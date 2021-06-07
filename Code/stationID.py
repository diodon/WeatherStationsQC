## Get AIMS weather Station ID, name and metadata record link
import json
import requests
import prettytable

AIMSurl = "https://api.aims.gov.au/weather/latestreadings"
WSjson = json.loads(requests.get(AIMSurl).text)

tbl = prettytable.PrettyTable(['Station Name', "Station ID", "Metadata url"])
for station in range(len(WSjson)):
    tbl.add_row([WSjson[station]['site_name'], WSjson[station]['site_id'], WSjson[station]['metadata']])

print(tbl)
