import json
import requests
import prettytable

## get the latest data using AIMS WS wer service
AIMSurl = "https://api.aims.gov.au/weather/latestreadings"
WSjson = json.loads(requests.get(AIMSurl).text)

## print the online status of each of the stations
tbl = prettytable.PrettyTable(["ID", "STATION", "STATUS"])
for item in range(len(WSjson)):
    if WSjson[item]['status']['online'] == 'true':
        status = 'ONLINE'
    else:
        status = 'OFFLINE'
    tbl.add_row([WSjson[item]['site_id'], WSjson[item]['site_name'], status])

print(tbl)

