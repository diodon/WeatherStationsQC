import warnings
warnings.filterwarnings('ignore')

import argparse
import json
import requests
import numpy as np
import prettytable
from sparklines import sparklines

def args():
    parser = argparse.ArgumentParser(description="AIMS weather station summary: latest readings.")
    parser.add_argument('-site', dest='site', help='site ID',  type=str, default=None, required=True)
    parser.add_argument('-noplot', dest='screen_plot', help='do not plot the latest readings', action='store_false',
                        required=False)
    vargs = parser.parse_args()
    return vargs


def WSsummary(site, screen_plot):
    '''
    Produce a summary of the recent data from a AIMS weather station
    :param site: site ID
    :return: nothing
    '''
    try:
        AIMSurl = "https://api.aims.gov.au/weather/station/" + str(site)
        WSjson = json.loads(requests.get(AIMSurl).text)
        print("Station ID: {id}".format(id=WSjson['site_id']))
        print("Station Name: {stName}".format(stName=WSjson['site_name']))
        print("Station location: {lon}LON, {lat}LAT".format(lon=WSjson['longitude'], lat=WSjson['latitude']))
        print("Station metadata record: {metadata}".format(metadata=WSjson['metadata']))
        if WSjson['status']['online'] == 'true':
            WSstatus = 'ONLINE'
        else:
            WSstatus = 'OFFLINE'
        WSstatusMessage = WSjson['status']['message']
        print("Current Status: {status}: {statusText}".format(status=WSstatus, statusText=WSstatusMessage))
        parameterList = list(WSjson['series'].keys())
        tbl = prettytable.PrettyTable()
        for param in parameterList:
            paramName = WSjson['series'][param]['parameterName']
            minutesAgo = WSjson['series'][param]['minutesAgo']
            paramUnits = WSjson['series'][param]['uomSymbol']
            if len(WSjson['series'][param]['data12Hours']) > 0:
                WSdata = WSjson['series'][param]['data12Hours']
                plotType = 'last 12 Hourly values'
            elif len(WSjson['series'][param]['data7Days']) > 0:
                WSdata = WSjson['series'][param]['data7Days']
                plotType = 'Daily averages'
            else:
                print("NO DATA AVAILABLE")
                return
            WSdate = []
            WSvalue = []
            for item in WSdata:
                WSdate.append(item['date'])
                WSvalue.append(item['qc'])
            paramLastDate = WSdate[-1]
            paramLastValue = WSvalue[-1]
            if screen_plot:
                paramPlot = []
                for v in sparklines(WSvalue):
                    paramPlot.append(v)
                paramPlot = paramPlot[0]
                #if plotType=="Daily averages":
                paramPlot = paramPlot[len(paramPlot)-25:]
                tbl.add_row([paramName, paramUnits, minutesAgo, paramLastDate, paramLastValue, paramPlot])
            else:
                paramPlot = ""
                tbl.add_row([paramName, paramUnits, minutesAgo, paramLastDate, paramLastValue])

        if screen_plot:
            tbl.field_names = ['Parameter', 'Units', 'Last Read (min ago)', 'Last Date', 'Last Value', 'Plot ' + plotType]
        else:
            tbl.field_names = ['Parameter', 'Units', 'Last Read (min ago)', 'Last Date', 'Last Value']

        print(tbl)
    except Exception as e:
        print('ERROR: site ID not found')
    return







if __name__ == "__main__":
    vargs = args()
    WSsummary(vargs.site, vargs.screen_plot)

