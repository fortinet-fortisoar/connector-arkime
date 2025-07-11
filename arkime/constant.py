"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

BASELINE_VISIBLE = {
    "All Nodes": "all",
    "Actual Nodes": "actual",
    "Baseline Nodes": "actualold",
    "New Nodes": "new",
    "Baseline Nodes Only": "old"
}

BASELINE_DATE = {
    "Disabled": 0,
    "1× Query Range": "1x",
    "2× Query Range": "2x",
    "4× Query Range": "4x",
    "6× Query Range": "6x",
    "8× Query Range": "8x",
    "10× Query Range": "10x",
    "1 Hour": 1,
    "6 Hours": 6,
    "1 Day": 24,
    "2 Days": 48,
    "3 Days": 72,
    "1 Week": 168,
    "2 Weeks": 336,
    "1 Month": 720,
    "2 Months": 1440,
    "6 Months": 4380,
    "1 Year": 8760
}

FIELDS = {
    "IP Protocol": "ipProtocol",
    "Root ID": "rootId",
    "Total Data Bytes": "totDataBytes",
    "Client Bytes": "client.bytes",
    "Server Bytes": "server.bytes",
    "First Packet": "firstPacket",
    "Last Packet": "lastPacket",
    "Source IP": "source.ip",
    "Source Port": "source.port",
    "Destination IP": "destination.ip",
    "Destination Port": "destination.port",
    "Total Packets": "network.packets",
    "Source Packets": "source.packets",
    "Destination Packets": "destination.packets",
    "Total Bytes": "network.bytes",
    "Source Bytes": "source.bytes",
    "Destination Bytes": "destination.bytes",
    "Node": "node",
    "HTTP URI": "http.uri",
    "Source Country (ISO)": "source.geo.country_iso_code",
    "Destination Country (ISO)": "destination.geo.country_iso_code",
    "Email Subject": "email.subject",
    "Email Sender": "email.src",
    "Email Recipient": "email.dst",
    "Email Filename": "email.filename",
    "DNS Host": "dns.host",
    "Certificate": "cert",
    "IRC Channel": "irc.channel",
    "HTTP XFF GEO": "http.xffGEO"
}

BOUNDING = {
    "First Packet": "first",
    "Last Packet": "last",
    "Bounded (Both First and Last Inside Range)": "both",
    "Session Overlaps Time Window": "either",
    "Database (Stored Time Bounds)": "database"
}
