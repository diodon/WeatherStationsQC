import datetime as dt
import json
import requests
import prettytable

RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
END = '\033[0m'


## get the latest data using AIMS WS wer service
AIMSurl = "https://api.aims.gov.au/weather/latestreadings"
WSjson = json.loads(requests.get(AIMSurl).text)

## print the online status of each of the stations
tbl = prettytable.PrettyTable(["ID", "STATION", "STATUS", "LAST READING", "PARAMETERS"])
for item in range(len(WSjson)):
    if WSjson[item]['status']['online'] == 'true':
        status = BLUE + 'ONLINE' + END
    else:
        status = RED + 'OFFLINE' + END
    paramList = []
    for ss in WSjson[item]['series']:
        if WSjson[item]['series'][ss]['status']['online'] == 'true':
            paramList.append(BLUE + ss + END)
        else:
            paramList.append(RED + ss + END)

    lastRead = WSjson[item]['series'][ss]['data']['date']
    tbl.add_row([WSjson[item]['site_id'], WSjson[item]['site_name'], status, lastRead, ", ".join(paramList)])

tbl.align["PARAMETERS"] = "l"
print(tbl)

