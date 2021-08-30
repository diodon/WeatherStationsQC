# WeatherStationsQC

Python and R functions to explore and perform quality control of data from AIMS weather stations

For the QC protocols, a JSON template for threshold values is drafted. Threshold values need to be read and passed to the functions.

`stationID.py`

Get the station ID. The ID is the argument to be passed to the python function. Just run this as your first option

`AIMSweather_status`

Current operation status of the weather stations

`WSsummary.py`

    usage: WSsummary.py [-h] -site SITE

    AIMS weather station summary: latest readings.

    optional arguments:
      -h, --help  show this help message and exit
      -site SITE  site ID
