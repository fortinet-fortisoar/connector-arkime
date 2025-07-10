"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

import requests, json
from requests.auth import HTTPDigestAuth
from datetime import datetime, timezone
from .constant import *
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('arkime')


class Arkime(object):
    def __init__(self, config, *args, **kwargs):
        self.username = config.get('username')
        self.password = config.get('password')
        url = config.get('server_url').strip('/')
        if not url.startswith('https://') and not url.startswith('http://'):
            self.url = 'https://{0}/api/'.format(url)
        else:
            self.url = url + '/api/'
        self.headers = {
            'Content-Type': 'application/json'
        }
        self.verify_ssl = config.get('verify_ssl')

    def make_rest_call(self, endpoint, method, data=None, params=None):
        try:
            url = self.url + endpoint
            logger.debug("Endpoint {0}".format(url))
            response = requests.request(method, url, data=data, params=params,
                                        auth=HTTPDigestAuth(self.username, self.password),
                                        headers=self.headers, verify=self.verify_ssl)
            logger.debug("response_content {0}:{1}".format(response.status_code, response.content))
            if response.ok or response.status_code == 204:
                logger.info('Successfully got response for url {0}'.format(url))
                if 'application/json' in response.headers.get('Content-Type', ''):
                    return response.json()
                else:
                    return response.text
            else:
                logger.error("{0}".format(response.status_code))
                raise ConnectorError("{0}:{1}".format(response.status_code, response.text))
        except requests.exceptions.SSLError:
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout:
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout:
            raise ConnectorError(
                'The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError:
            raise ConnectorError('Invalid Credentials')
        except Exception as err:
            raise ConnectorError(str(err))


def check_payload(payload):
    updated_payload = {}
    for key, value in payload.items():
        if isinstance(value, dict):
            nested = check_payload(value)
            if len(nested.keys()) > 0:
                updated_payload[key] = nested
        elif value != '' and value is not None:
            updated_payload[key] = value
    return updated_payload


def convert_datetime_to_epoch(date_time):
    formats = [
        "%Y-%m-%dT%H:%M:%S.%fZ",  # with microseconds and Z (UTC)
        "%Y-%m-%dT%H:%M:%S.%f",  # with microseconds, no Z
        "%Y-%m-%dT%H:%M:%S.%f%z",  # microseconds with offset (if Z is replaced with +0000)
    ]
    for fmt in formats:
        try:
            dt = datetime.strptime(date_time, fmt).replace(tzinfo=timezone.utc)
            epoch_seconds = int(dt.timestamp())
            return epoch_seconds
        except ValueError:
            continue
    else:
        raise ConnectorError("No matching date format found")


def convert_fields_to_list(fields_string):
    fields = []
    for field in fields_string:
        value = FIELDS.get(field)
        if value is not None:
            fields.append(value)
    return fields


def convert_bounding_to_list(bounding_string):
    boundings = []
    for bounding in bounding_string:
        value = BOUNDING.get(bounding)
        if value is not None:
            boundings.append(value)
    return boundings


def build_query_parameters(params):
    start_time = params.get('startTime')
    if start_time and 'T' in start_time:
        start_time = convert_datetime_to_epoch(start_time)
    stop_time = params.get('stopTime')
    if stop_time and 'T' in stop_time:
        stop_time = convert_datetime_to_epoch(stop_time)
    fields = convert_fields_to_list(params.get('fields')) if params.get('fields') else []
    boundings = convert_bounding_to_list(params.get('bounding')) if params.get('bounding') else []
    build_query_parameter = {
        "date": params.get('date'),
        "expression": params.get('expression', ''),
        "facets": params.get('facets'),
        "length": params.get('length'),
        "start": params.get('start'),
        "startTime": start_time,
        "stopTime": stop_time,
        "view": params.get('view'),
        "order": params.get('order').split(",") if params.get('order') else [],
        "fields": fields,
        "bounding": boundings,
        "strictly": params.get('strictly')
    }
    return build_query_parameter


def get_all_connections(config, params):
    try:
        ark = Arkime(config)
        endpoint = 'connections'
        payload = {
            "srcField": params.get('srcField'),
            "dstField": params.get('dstField'),
            "baselineDate": BASELINE_DATE.get(params.get('baselineDate')),
            "baselineVis": BASELINE_VISIBLE.get(params.get('baselineVis'))
        }
        payload.update(build_query_parameters(params))
        query_parameter = check_payload(payload)
        logger.debug("Payload {0}".format(query_parameter))
        response = ark.make_rest_call(endpoint, 'POST', params=query_parameter)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def get_all_connections_csv(config, params):
    try:
        ark = Arkime(config)
        endpoint = 'connections/csv'
        payload = {
            "srcField": params.get('srcField'),
            "dstField": params.get('dstField')
        }
        payload.update(build_query_parameters(params))
        query_parameter = check_payload(payload)
        logger.debug("Payload {0}".format(query_parameter))
        response = ark.make_rest_call(endpoint, 'POST', params=query_parameter)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def get_all_pcap_files(config, params):
    try:
        ark = Arkime(config)
        endpoint = 'files'
        payload = {
            "length": params.get('length'),
            "start": params.get('start')
        }
        query_parameter = check_payload(payload)
        logger.debug("Payload {0}".format(query_parameter))
        response = ark.make_rest_call(endpoint, 'GET', params=query_parameter)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def get_all_sessions(config, params):
    try:
        ark = Arkime(config)
        endpoint = 'sessions'
        query_parameter = check_payload(build_query_parameters(params))
        logger.debug("Payload {0}".format(query_parameter))
        response = ark.make_rest_call(endpoint, 'POST', params=query_parameter)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def get_all_sessions_csv(config, params):
    try:
        ark = Arkime(config)
        endpoint = 'sessions/csv'
        payload = {
            "ids": params.get('ids').split(",") if params.get('ids') else ''
        }
        payload.update(build_query_parameters(params))
        query_parameter = check_payload(payload)
        logger.debug("Payload {0}".format(query_parameter))
        response = ark.make_rest_call(endpoint, 'POST', params=query_parameter)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def get_all_sessions_pcap(config, params):
    try:
        ark = Arkime(config)
        endpoint = 'sessions/pcap'
        payload = {
            "ids": params.get('ids').split(",") if params.get('ids') else '',
            "segments": params.get('segments')
        }
        payload.update(build_query_parameters(params))
        query_parameter = check_payload(payload)
        logger.debug("Payload {0}".format(query_parameter))
        response = ark.make_rest_call(endpoint, 'GET', params=query_parameter)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def get_all_spi_graph(config, params):
    try:
        ark = Arkime(config)
        endpoint = 'spigraph'
        query_parameter = check_payload(build_query_parameters(params))
        logger.debug("Payload {0}".format(query_parameter))
        response = ark.make_rest_call(endpoint, 'POST', params=query_parameter)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def get_all_spi_view(config, params):
    try:
        ark = Arkime(config)
        endpoint = 'spiview'
        payload = {
            "spi": params.get('spi').split(",") if params.get('spi') else ''
        }
        payload.update(build_query_parameters(params))
        query_parameter = check_payload(payload)
        logger.debug("Payload {0}".format(query_parameter))
        response = ark.make_rest_call(endpoint, 'POST', params=query_parameter)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def get_all_fields(config, params):
    try:
        ark = Arkime(config)
        endpoint = 'fields'
        payload = {
            "array": params.get('array')
        }
        query_parameter = check_payload(payload)
        logger.debug("Payload {0}".format(query_parameter))
        response = ark.make_rest_call(endpoint, 'GET', params=query_parameter)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def get_all_unique_fields(config, params):
    try:
        ark = Arkime(config)
        endpoint = 'unique'
        payload = {
            "counts": params.get('counts'),
            "exp": params.get('exp')
        }
        payload.update(build_query_parameters(params))
        query_parameter = check_payload(payload)
        logger.debug("Payload {0}".format(query_parameter))
        response = ark.make_rest_call(endpoint, 'POST', params=query_parameter)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def get_all_multiple_unique_fields(config, params):
    try:
        ark = Arkime(config)
        endpoint = 'multiunique'
        payload = {
            "counts": params.get('counts'),
            "exp": params.get('exp').split(",") if params.get('exp') else ''
        }
        payload.update(build_query_parameters(params))
        query_parameter = check_payload(payload)
        logger.debug("Payload {0}".format(query_parameter))
        response = ark.make_rest_call(endpoint, 'POST', params=query_parameter)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def add_tags_to_sessions(config, params):
    try:
        ark = Arkime(config)
        endpoint = 'sessions/addtags'
        payload = {
            "tags": params.get('tags').split(",") if params.get('tags') else '',
            "ids": params.get('ids').split(",") if params.get('ids') else '',
            "segments": params.get('segments')
        }
        payload.update(build_query_parameters(params))
        query_parameter = check_payload(payload)
        logger.debug("Payload {0}".format(query_parameter))
        response = ark.make_rest_call(endpoint, 'POST', params=query_parameter)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def remove_tags_from_sessions(config, params):
    try:
        ark = Arkime(config)
        endpoint = 'sessions/removetags'
        payload = {
            "tags": params.get('tags').split(",") if params.get('tags') else '',
            "ids": params.get('ids').split(",") if params.get('ids') else '',
            "segments": params.get('segments')
        }
        payload.update(build_query_parameters(params))
        query_parameter = check_payload(payload)
        logger.debug("Payload {0}".format(query_parameter))
        response = ark.make_rest_call(endpoint, 'POST', params=query_parameter)
        return response
    except Exception as err:
        raise ConnectorError(str(err))


def execute_an_api_call(config, params):
    try:
        ark = Arkime(config)
        endpoint = params.get("endpoint")
        http_method = params.get("method")
        query_params = params.get("query_params") if params.get("query_params") else {}
        payload = params.get("payload") if params.get("payload") else {}
        logger.debug("Payload: {0}".format(payload))
        response = ark.make_rest_call(endpoint, method=http_method, params=query_params, data=json.dumps(payload))
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def check_health(config):
    try:
        response = get_all_connections(config, params={'length': 1})
        if response:
            return True
    except Exception as err:
        logger.info(str(err))
        raise ConnectorError(str(err))


operations = {
    'get_all_connections': get_all_connections,
    'get_all_connections_csv': get_all_connections_csv,
    'get_all_pcap_files': get_all_pcap_files,
    'get_all_sessions': get_all_sessions,
    'get_all_sessions_csv': get_all_sessions_csv,
    'get_all_sessions_pcap': get_all_sessions_pcap,
    'get_all_spi_graph': get_all_spi_graph,
    'get_all_spi_view': get_all_spi_view,
    'get_all_fields': get_all_fields,
    'get_all_unique_fields': get_all_unique_fields,
    'get_all_multiple_unique_fields': get_all_multiple_unique_fields,
    'add_tags_to_sessions': add_tags_to_sessions,
    'remove_tags_from_sessions': remove_tags_from_sessions,
    'execute_an_api_call': execute_an_api_call
}
