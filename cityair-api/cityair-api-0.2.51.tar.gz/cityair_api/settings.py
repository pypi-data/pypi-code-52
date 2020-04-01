LOGIN_VAR_NAME = 'CITYAIR_LOGIN'
PSW_VAR_NAME = 'CITYAIR_PSW'

DEFAULT_HOST = "https://cityair.io/backend-api/request-v2.php?map="
DEVICES_URL = "DevicesApi2/GetDevices"
DEVICES_PACKETS_URL = "DevicesApi2/GetPackets"
STATIONS_URL = "MoApi2/GetMoItems"
STATIONS_PACKETS_URL = "MoApi2/GetMoPackets"
LOGS_URL = "/LoggerApi/GetLogItems"
FULL_LOGS_URL ="/LoggerApi/GetFullLogItems"

PACKET_SENDER_IDS = [{"AppId": 4, "SenderIds": [23]}]  # for logs lookups

LOG_CHECKINFO_FILTER_PATTERN = "#CheckInfo#{[^']*}"
LOG_CHECKINFO_ADDITIONAL_FILTER_SUFFIX = " CheckInfo"
LOG_PACKET_FILTER_PATTERN = r"#PT#\d+"
LOG_PACKET_ADDITIONAL_FILTER_SUFFIX = " PT"
LOG_EXTRACT_PATTERN = r"#([^']*)\n##"
CHECKINFO_PARSE_PATTERN = r"#CheckInfo#{([^'\n]*)}\n"