## About the connector
Arkime is an open-source, large-scale, full packet capture (FPC) and indexing system. It's designed for security professionals to store and analyze network traffic in detail.
<p>This document provides information about the Arkime Connector, which facilitates automated interactions, with a Arkime server using FortiSOAR&trade; playbooks. Add the Arkime Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Arkime.</p>

### Version information

Connector Version: 1.0.0

Authored By: Fortinet

Certified: No

## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-arkime`

## Prerequisites to configuring the connector
- You must have the URL of Arkime server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Arkime server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Arkime</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the URL of the Arkime server to connect and perform automated operations.<br>
<tr><td>Username<br></td><td>Specify the username to connect to the endpoint and perform automated operations<br>
<tr><td>Password<br></td><td>Specify the password to connect to the endpoint and perform automated operations<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get All Connections<br></td><td>Retrieves a list of nodes and links from Arkime based on the filter parameters that you have specified.<br></td><td>get_all_connections <br/>Investigation<br></td></tr>
<tr><td>Get All Connections CSV<br></td><td>Retrieves a list of nodes and links in CSV format from Arkime based on the filter parameters that you have specified.<br></td><td>get_all_connections_csv <br/>Investigation<br></td></tr>
<tr><td>Get All PCAP Files<br></td><td>Retrieves a list of PCAP files from Arkime based on the filter parameters that you have specified.<br></td><td>get_all_pcap_files <br/>Investigation<br></td></tr>
<tr><td>Get All Sessions<br></td><td>Retrieves a list of sessions from Arkime based on the filter parameters that you have specified.<br></td><td>get_all_sessions <br/>Investigation<br></td></tr>
<tr><td>Get All Sessions CSV<br></td><td>Retrieves a list of sessions in CSV format from Arkime based on the filter parameters that you have specified.<br></td><td>get_all_sessions_csv <br/>Investigation<br></td></tr>
<tr><td>Get All Sessions PCAP<br></td><td>Retrieves a list of raw session data in PCAP format from Arkime based on the filter parameters that you have specified.<br></td><td>get_all_sessions_pcap <br/>Investigation<br></td></tr>
<tr><td>Get All SPI Graph<br></td><td>Retrieves a list of values for a field with counts and graph data from Arkime based on the filter parameters that you have specified.<br></td><td>get_all_spi_graph <br/>Investigation<br></td></tr>
<tr><td>Get All SPI View<br></td><td>Retrieves a list of field values with counts from Arkime based on the filter parameters that you have specified.<br></td><td>get_all_spi_view <br/>Investigation<br></td></tr>
<tr><td>Get All Fields<br></td><td>Retrieves a available database field objects pertaining to sessions from Arkime.<br></td><td>get_all_fields <br/>Investigation<br></td></tr>
<tr><td>Get All Unique Fields<br></td><td>Retrieves a list of unique field values (with or without counts) from Arkime based on the filter parameters that you have specified.<br></td><td>get_all_unique_fields <br/>Investigation<br></td></tr>
<tr><td>Get All Multiple Unique Fields<br></td><td>Retrieves an intersection of unique field values (with or without counts) from Arkime based on the filter parameters that you have specified.<br></td><td>get_all_multiple_unique_fields <br/>Investigation<br></td></tr>
<tr><td>Add Tags to Sessions<br></td><td>Add tag(s) to individual session(s) by id or by query in Arkime based on the filter parameters that you have specified.<br></td><td>add_tags_to_sessions <br/>Investigation<br></td></tr>
<tr><td>Remove Tags from Sessions<br></td><td>Removes tag(s) from individual session(s) by id or by query on Arkime based on the filter parameters that you have specified.<br></td><td>remove_tags_from_sessions <br/>Investigation<br></td></tr>
<tr><td>Execute an API Request<br></td><td>Sends an API request to an API endpoint based on specified HTTP method, endpoint, and other input parameters that you have specified, enabling flexible API interactions tailored to user needs.<br></td><td>execute_an_api_call <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Get All Connections
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Source Field<br></td><td>Specify the source database field name based on which you want to retrieve connections.<br>
</td></tr><tr><td>Destination Field<br></td><td>Specify the destination database field name based on which you want to retrieve connections.<br>
</td></tr><tr><td>Baseline Date<br></td><td>Select the baseline date range to compare connections. Possible values are Disabled, 1× Query Range, 2× Query Range, 4× Query Range, etc. By default, this option is set as "Disabled".<br>
</td></tr><tr><td>Baseline Visible<br></td><td>Select the connections to display when a baseline date range is applied. Possible values are All Nodes, Actual Nodes, Baseline Nodes, New Nodes, or Baseline Nodes Only. By default, this option is set as "All Nodes".<br>
</td></tr><tr><td>Relative Time (Hours Ago)<br></td><td>Search from a specified number of hours ago until now. Use -1 to search all data. By default, this option is set as 1.<br>
</td></tr><tr><td>Search Expression<br></td><td>Specify the search expression string based on which you want to retrieve connections.<br>
</td></tr><tr><td>Arkime View<br></td><td>Specify the view name of the arkime to apply before the expression.<br>
</td></tr><tr><td>Include Aggregations<br></td><td>Set to 1 to include aggregation info for maps and timeline graphs. By default, this option is set as 0.<br>
</td></tr><tr><td>Start DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created after the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Stop DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created before the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Sort Order<br></td><td>Specify a comma-separated list of field names to sort the results by. Each field can optionally be followed by :asc for ascending or :desc for descending order.<br>
</td></tr><tr><td>Fields to Return<br></td><td>Select one or more database field names to include in the response. Possible values are IP Protocol, Root ID, Total Data Bytes, etc<br>
</td></tr><tr><td>Time Bounding<br></td><td>Select the time bounding mode for session search. Possible values are First Packet, Last Packet, Bounded (Both First and Last Inside Range), Session Overlaps Time Window, or Database (Stored Time Bounds). By default, this option is set as "Last Packet".<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum number of results, per page, that this operation should return. By default, this option is set as 100 and maximum is 2,000,000.<br>
</td></tr><tr><td>Offset<br></td><td>Index of the first item to be returned by this operation. This parameter is useful for pagination and for getting a subset of items. By default, this is set as 0<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get All Connections CSV
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Source Field<br></td><td>Specify the source database field name based on which you want to retrieve connections csv.<br>
</td></tr><tr><td>Destination Field<br></td><td>Specify the destination database field name based on which you want to retrieve connections csv.<br>
</td></tr><tr><td>Relative Time (Hours Ago)<br></td><td>Search from a specified number of hours ago until now. Use -1 to search all data. By default, this option is set as 1.<br>
</td></tr><tr><td>Search Expression<br></td><td>Specify the search expression string based on which you want to retrieve connections csv.<br>
</td></tr><tr><td>Arkime View<br></td><td>Specify the view name of the arkime to apply before the expression.<br>
</td></tr><tr><td>Include Aggregations<br></td><td>Set to 1 to include aggregation info for maps and timeline graphs. By default, this option is set as 0.<br>
</td></tr><tr><td>Start DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created after the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Stop DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created before the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Sort Order<br></td><td>Specify a comma-separated list of field names to sort the results by. Each field can optionally be followed by :asc for ascending or :desc for descending order.<br>
</td></tr><tr><td>Fields to Return<br></td><td>Select one or more database field names to include in the response. Possible values are IP Protocol, Root ID, Total Data Bytes, etc<br>
</td></tr><tr><td>Time Bounding<br></td><td>Select the time bounding mode for session search. Possible values are First Packet, Last Packet, Bounded (Both First and Last Inside Range), Session Overlaps Time Window, or Database (Stored Time Bounds). By default, this option is set as "Last Packet".<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum number of results, per page, that this operation should return. By default, this option is set as 100 and maximum is 2,000,000.<br>
</td></tr><tr><td>Offset<br></td><td>Index of the first item to be returned by this operation. This parameter is useful for pagination and for getting a subset of items. By default, this is set as 0<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get All PCAP Files
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Limit<br></td><td>Specify the maximum number of results, per page, that this operation should return. By default, this option is set as 100 and maximum is 2,000,000.<br>
</td></tr><tr><td>Offset<br></td><td>Index of the first item to be returned by this operation. This parameter is useful for pagination and for getting a subset of items. By default, this is set as 0<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get All Sessions
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Relative Time (Hours Ago)<br></td><td>Search from a specified number of hours ago until now. Use -1 to search all data. By default, this option is set as 1.<br>
</td></tr><tr><td>Search Expression<br></td><td>Specify the search expression string based on which you want to retrieve sessions.<br>
</td></tr><tr><td>Arkime View<br></td><td>Specify the view name of the arkime to apply before the expression.<br>
</td></tr><tr><td>Include Aggregations<br></td><td>Set to 1 to include aggregation info for maps and timeline graphs. By default, this option is set as 0.<br>
</td></tr><tr><td>Start DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created after the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Stop DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created before the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Sort Order<br></td><td>Specify a comma-separated list of field names to sort the results by. Each field can optionally be followed by :asc for ascending or :desc for descending order.<br>
</td></tr><tr><td>Fields to Return<br></td><td>Select one or more database field names to include in the response. Possible values are IP Protocol, Root ID, Total Data Bytes, etc<br>
</td></tr><tr><td>Time Bounding<br></td><td>Select the time bounding mode for session search. Possible values are First Packet, Last Packet, Bounded (Both First and Last Inside Range), Session Overlaps Time Window, or Database (Stored Time Bounds). By default, this option is set as "Last Packet".<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum number of results, per page, that this operation should return. By default, this option is set as 100 and maximum is 2,000,000.<br>
</td></tr><tr><td>Offset<br></td><td>Index of the first item to be returned by this operation. This parameter is useful for pagination and for getting a subset of items. By default, this is set as 0<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get All Sessions CSV
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Session IDs<br></td><td>Specify the comma separated list of sessions to retrieve.<br>
</td></tr><tr><td>Relative Time (Hours Ago)<br></td><td>Search from a specified number of hours ago until now. Use -1 to search all data. By default, this option is set as 1.<br>
</td></tr><tr><td>Search Expression<br></td><td>Specify the search expression string based on which you want to retrieve sessions csv.<br>
</td></tr><tr><td>Arkime View<br></td><td>Specify the view name of the arkime to apply before the expression.<br>
</td></tr><tr><td>Include Aggregations<br></td><td>Set to 1 to include aggregation info for maps and timeline graphs. By default, this option is set as 0.<br>
</td></tr><tr><td>Start DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created after the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Stop DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created before the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Sort Order<br></td><td>Specify a comma-separated list of field names to sort the results by. Each field can optionally be followed by :asc for ascending or :desc for descending order.<br>
</td></tr><tr><td>Fields to Return<br></td><td>Select one or more database field names to include in the response. Possible values are IP Protocol, Root ID, Total Data Bytes, etc<br>
</td></tr><tr><td>Time Bounding<br></td><td>Select the time bounding mode for session search. Possible values are First Packet, Last Packet, Bounded (Both First and Last Inside Range), Session Overlaps Time Window, or Database (Stored Time Bounds). By default, this option is set as "Last Packet".<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum number of results, per page, that this operation should return. By default, this option is set as 100 and maximum is 2,000,000.<br>
</td></tr><tr><td>Offset<br></td><td>Index of the first item to be returned by this operation. This parameter is useful for pagination and for getting a subset of items. By default, this is set as 0<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get All Sessions PCAP
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Session IDs<br></td><td>Specify the comma separated list of sessions to retrieve in pcap.<br>
</td></tr><tr><td>Segments<br></td><td>If this option is selected, the response will include linked segments.<br>
</td></tr><tr><td>Relative Time (Hours Ago)<br></td><td>Search from a specified number of hours ago until now. Use -1 to search all data. By default, this option is set as 1.<br>
</td></tr><tr><td>Search Expression<br></td><td>Specify the search expression string based on which you want to retrieve sessions in pcap.<br>
</td></tr><tr><td>Arkime View<br></td><td>Specify the view name of the arkime to apply before the expression.<br>
</td></tr><tr><td>Include Aggregations<br></td><td>Set to 1 to include aggregation info for maps and timeline graphs. By default, this option is set as 0.<br>
</td></tr><tr><td>Start DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created after the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Stop DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created before the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Sort Order<br></td><td>Specify a comma-separated list of field names to sort the results by. Each field can optionally be followed by :asc for ascending or :desc for descending order.<br>
</td></tr><tr><td>Fields to Return<br></td><td>Select one or more database field names to include in the response. Possible values are IP Protocol, Root ID, Total Data Bytes, etc<br>
</td></tr><tr><td>Time Bounding<br></td><td>Select the time bounding mode for session search. Possible values are First Packet, Last Packet, Bounded (Both First and Last Inside Range), Session Overlaps Time Window, or Database (Stored Time Bounds). By default, this option is set as "Last Packet".<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum number of results, per page, that this operation should return. By default, this option is set as 100 and maximum is 2,000,000.<br>
</td></tr><tr><td>Offset<br></td><td>Index of the first item to be returned by this operation. This parameter is useful for pagination and for getting a subset of items. By default, this is set as 0<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get All SPI Graph
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Relative Time (Hours Ago)<br></td><td>Search from a specified number of hours ago until now. Use -1 to search all data. By default, this option is set as 1.<br>
</td></tr><tr><td>Search Expression<br></td><td>Specify the search expression string based on which you want to retrieve spi graph details.<br>
</td></tr><tr><td>Arkime View<br></td><td>Specify the view name of the arkime to apply before the expression.<br>
</td></tr><tr><td>Include Aggregations<br></td><td>Set to 1 to include aggregation info for maps and timeline graphs. By default, this option is set as 0.<br>
</td></tr><tr><td>Start DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created after the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Stop DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created before the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Sort Order<br></td><td>Specify a comma-separated list of field names to sort the results by. Each field can optionally be followed by :asc for ascending or :desc for descending order.<br>
</td></tr><tr><td>Fields to Return<br></td><td>Select one or more database field names to include in the response. Possible values are IP Protocol, Root ID, Total Data Bytes, etc<br>
</td></tr><tr><td>Time Bounding<br></td><td>Select the time bounding mode for session search. Possible values are First Packet, Last Packet, Bounded (Both First and Last Inside Range), Session Overlaps Time Window, or Database (Stored Time Bounds). By default, this option is set as "Last Packet".<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum number of results, per page, that this operation should return. By default, this option is set as 100 and maximum is 2,000,000.<br>
</td></tr><tr><td>Offset<br></td><td>Index of the first item to be returned by this operation. This parameter is useful for pagination and for getting a subset of items. By default, this is set as 0<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get All SPI View
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>SPI<br></td><td>Specify the comma separated list of db fields to return. Optionally can be followed by :{count} to specify the number of values returned for the field (defaults to 100).<br>
</td></tr><tr><td>Relative Time (Hours Ago)<br></td><td>Search from a specified number of hours ago until now. Use -1 to search all data. By default, this option is set as 1.<br>
</td></tr><tr><td>Search Expression<br></td><td>Specify the search expression string based on which you want to retrieve spi view.<br>
</td></tr><tr><td>Arkime View<br></td><td>Specify the view name of the arkime to apply before the expression.<br>
</td></tr><tr><td>Include Aggregations<br></td><td>Set to 1 to include aggregation info for maps and timeline graphs. By default, this option is set as 0.<br>
</td></tr><tr><td>Start DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created after the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Stop DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created before the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Sort Order<br></td><td>Specify a comma-separated list of field names to sort the results by. Each field can optionally be followed by :asc for ascending or :desc for descending order.<br>
</td></tr><tr><td>Fields to Return<br></td><td>Select one or more database field names to include in the response. Possible values are IP Protocol, Root ID, Total Data Bytes, etc<br>
</td></tr><tr><td>Time Bounding<br></td><td>Select the time bounding mode for session search. Possible values are First Packet, Last Packet, Bounded (Both First and Last Inside Range), Session Overlaps Time Window, or Database (Stored Time Bounds). By default, this option is set as "Last Packet".<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum number of results, per page, that this operation should return. By default, this option is set as 100 and maximum is 2,000,000.<br>
</td></tr><tr><td>Offset<br></td><td>Index of the first item to be returned by this operation. This parameter is useful for pagination and for getting a subset of items. By default, this is set as 0<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get All Fields
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Array<br></td><td>If this option is selected, the response will return an array of fields, otherwise returns a map.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get All Unique Fields
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Counts<br></td><td>Whether to return counts with he list of unique field values. Defaults to 0. 0 = no counts, 1 - counts.<br>
</td></tr><tr><td>Expression Field<br></td><td>Specify the expression field to return unique data from arkime.<br>
</td></tr><tr><td>Relative Time (Hours Ago)<br></td><td>Search from a specified number of hours ago until now. Use -1 to search all data. By default, this option is set as 1.<br>
</td></tr><tr><td>Search Expression<br></td><td>Specify the search expression string based on which you want to retrieve unique fields.<br>
</td></tr><tr><td>Arkime View<br></td><td>Specify the view name of the arkime to apply before the expression.<br>
</td></tr><tr><td>Include Aggregations<br></td><td>Set to 1 to include aggregation info for maps and timeline graphs. By default, this option is set as 0.<br>
</td></tr><tr><td>Start DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created after the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Stop DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created before the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Sort Order<br></td><td>Specify a comma-separated list of field names to sort the results by. Each field can optionally be followed by :asc for ascending or :desc for descending order.<br>
</td></tr><tr><td>Fields to Return<br></td><td>Select one or more database field names to include in the response. Possible values are IP Protocol, Root ID, Total Data Bytes, etc<br>
</td></tr><tr><td>Time Bounding<br></td><td>Select the time bounding mode for session search. Possible values are First Packet, Last Packet, Bounded (Both First and Last Inside Range), Session Overlaps Time Window, or Database (Stored Time Bounds). By default, this option is set as "Last Packet".<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum number of results, per page, that this operation should return. By default, this option is set as 100 and maximum is 2,000,000.<br>
</td></tr><tr><td>Offset<br></td><td>Index of the first item to be returned by this operation. This parameter is useful for pagination and for getting a subset of items. By default, this is set as 0<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get All Multiple Unique Fields
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Counts<br></td><td>Whether to return counts with he list of unique field values. Defaults to 0. 0 = no counts, 1 - counts.<br>
</td></tr><tr><td>Expression Field<br></td><td>Specify the comma separated list of expression fields to return unique data from arkime.<br>
</td></tr><tr><td>Relative Time (Hours Ago)<br></td><td>Search from a specified number of hours ago until now. Use -1 to search all data. By default, this option is set as 1.<br>
</td></tr><tr><td>Search Expression<br></td><td>Specify the search expression string based on which you want to retrieve multiple unique fields.<br>
</td></tr><tr><td>Arkime View<br></td><td>Specify the view name of the arkime to apply before the expression.<br>
</td></tr><tr><td>Include Aggregations<br></td><td>Set to 1 to include aggregation info for maps and timeline graphs. By default, this option is set as 0.<br>
</td></tr><tr><td>Start DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created after the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Stop DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created before the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Sort Order<br></td><td>Specify a comma-separated list of field names to sort the results by. Each field can optionally be followed by :asc for ascending or :desc for descending order.<br>
</td></tr><tr><td>Fields to Return<br></td><td>Select one or more database field names to include in the response. Possible values are IP Protocol, Root ID, Total Data Bytes, etc<br>
</td></tr><tr><td>Time Bounding<br></td><td>Select the time bounding mode for session search. Possible values are First Packet, Last Packet, Bounded (Both First and Last Inside Range), Session Overlaps Time Window, or Database (Stored Time Bounds). By default, this option is set as "Last Packet".<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum number of results, per page, that this operation should return. By default, this option is set as 100 and maximum is 2,000,000.<br>
</td></tr><tr><td>Offset<br></td><td>Index of the first item to be returned by this operation. This parameter is useful for pagination and for getting a subset of items. By default, this is set as 0<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Add Tags to Sessions
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Sessions IDs<br></td><td>Specify the comma separated list of sessions to add tag(s)<br>
</td></tr><tr><td>Tags<br></td><td>Specify the comma separated list of tags to add to session(s)<br>
</td></tr><tr><td>Segments<br></td><td>Whether to add tags to linked session segments. Default is no. Options include: no - Don’t add tags to linked segments all - Add tags to all linked segments time - Add tags to segments occurring in the same time period<br>
</td></tr><tr><td>Relative Time (Hours Ago)<br></td><td>Search from a specified number of hours ago until now. Use -1 to search all data. By default, this option is set as 1.<br>
</td></tr><tr><td>Search Expression<br></td><td>Specify the search expression string based on which you want to add tags.<br>
</td></tr><tr><td>Arkime View<br></td><td>Specify the view name of the arkime to apply before the expression.<br>
</td></tr><tr><td>Include Aggregations<br></td><td>Set to 1 to include aggregation info for maps and timeline graphs. By default, this option is set as 0.<br>
</td></tr><tr><td>Start DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created after the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Stop DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created before the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Sort Order<br></td><td>Specify a comma-separated list of field names to sort the results by. Each field can optionally be followed by :asc for ascending or :desc for descending order.<br>
</td></tr><tr><td>Fields to Return<br></td><td>Select one or more database field names to include in the response. Possible values are IP Protocol, Root ID, Total Data Bytes, etc<br>
</td></tr><tr><td>Time Bounding<br></td><td>Select the time bounding mode for session search. Possible values are First Packet, Last Packet, Bounded (Both First and Last Inside Range), Session Overlaps Time Window, or Database (Stored Time Bounds). By default, this option is set as "Last Packet".<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum number of results, per page, that this operation should return. By default, this option is set as 100 and maximum is 2,000,000.<br>
</td></tr><tr><td>Offset<br></td><td>Index of the first item to be returned by this operation. This parameter is useful for pagination and for getting a subset of items. By default, this is set as 0<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Remove Tags from Sessions
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Sessions IDs<br></td><td>Specify the comma separated list of sessions to remove tag(s)<br>
</td></tr><tr><td>Tags<br></td><td>Specify the comma separated list of tags to remove from session(s)<br>
</td></tr><tr><td>Segments<br></td><td>Whether to remove tags from linked session segments. Default is no. Options include: no - Don’t remove tags from linked segments all - Remove tags from all linked segments time - Remove tags from segments occurring in the same time period<br>
</td></tr><tr><td>Relative Time (Hours Ago)<br></td><td>Search from a specified number of hours ago until now. Use -1 to search all data. By default, this option is set as 1.<br>
</td></tr><tr><td>Search Expression<br></td><td>Specify the search expression string based on which you want to remove tags.<br>
</td></tr><tr><td>Arkime View<br></td><td>Specify the view name of the arkime to apply before the expression.<br>
</td></tr><tr><td>Include Aggregations<br></td><td>Set to 1 to include aggregation info for maps and timeline graphs. By default, this option is set as 0.<br>
</td></tr><tr><td>Start DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created after the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Stop DateTime<br></td><td>Select the DateTime using which you want to filter the result set to only include only those items that have been created before the specified timestamp. Note: Used if "Relative Time (Hours Ago)" is not set.<br>
</td></tr><tr><td>Sort Order<br></td><td>Specify a comma-separated list of field names to sort the results by. Each field can optionally be followed by :asc for ascending or :desc for descending order.<br>
</td></tr><tr><td>Fields to Return<br></td><td>Select one or more database field names to include in the response. Possible values are IP Protocol, Root ID, Total Data Bytes, etc<br>
</td></tr><tr><td>Time Bounding<br></td><td>Select the time bounding mode for session search. Possible values are First Packet, Last Packet, Bounded (Both First and Last Inside Range), Session Overlaps Time Window, or Database (Stored Time Bounds). By default, this option is set as "Last Packet".<br>
</td></tr><tr><td>Limit<br></td><td>Specify the maximum number of results, per page, that this operation should return. By default, this option is set as 100 and maximum is 2,000,000.<br>
</td></tr><tr><td>Offset<br></td><td>Index of the first item to be returned by this operation. This parameter is useful for pagination and for getting a subset of items. By default, this is set as 0<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Execute an API Request
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>HTTP Method<br></td><td>Select an HTTP action for the request. You can select from the following options:  

DELETE 

GET 

PATCH 

POST 

PUT <br>
</td></tr><tr><td>Endpoint<br></td><td>Specify the target API URL path for the request. For example, if the website is https://example.com and URL path is https://example.com/images/pic.jpg, the endpoint would be images/pic.jpg.<br>
</td></tr><tr><td>Query Parameters<br></td><td>(Optional) Specify any optional parameters to add to the URL and refine the request.<br>
</td></tr><tr><td>Request Payload<br></td><td>(Optional) Specify data, as JSON, to be sent as the request payload (typically for POST or PUT requests).<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - Arkime - 1.0.0` playbook collection comes bundled with the Arkime connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Arkime connector.

- Get All Connections
- Get All Connections CSV
- Get All PCAP Files
- Get All Sessions
- Get All Sessions CSV
- Get All Sessions PCAP
- Get All SPI Graph
- Get All SPI View
- Get All Fields
- Get All Unique Fields
- Get All Multiple Unique Fields
- Add Tags to Sessions
- Remove Tags from Sessions
- Execute an API Request

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
