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


Example:

```
python WSsummary.py -site 1
Station ID: 1
Station Name: Agincourt Reef Number 3
Station location: 145.82251LON, -15.98278LAT
Station metadata record: https://apps.aims.gov.au/metadata/view/5ee39300-4ade-11dc-8f56-00008a07204e
Current Status: ONLINE: Some sensors have stopped operating
+-----------------------------+--------------+---------------------+---------------------------+------------+----------------------------+
|          Parameter          |    Units     | Last Read (min ago) |         Last Date         | Last Value | Plot last 12 Hourly values |
+-----------------------------+--------------+---------------------+---------------------------+------------+----------------------------+
|         Air Pressure        |     hpa      |          10         | 2021-08-30T04:50:00+10:00 |   1010.7   | ▇▇▇▇▇▆▆▆▅▅▄▄▄▄▄▃▃▃▂▂▂▂▁▁▁  |
|       Air Temperature       |      °C      |          10         | 2021-08-30T04:50:00+10:00 |    24.9    | ▄▄▄▅▄▃▅▅▄▄▃▃▃▄▂▂▂▂▁▂▂▁▂▁▁  |
|           Humidity          |      %       |          0          | 2021-08-30T04:50:00+10:00 |    85.9    | ▃▃▃▃▄▄▄▃▃▃▂▁▃▂▃▁▃▃▃▂▃▅▂▃▂  |
|             PAR             | umol s-¹ m-² |          10         | 2021-08-30T04:50:00+10:00 |  19.3136   | ▄▃▃▃▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁  |
| Rain Accumulation since 9am |      mm      |          10         | 2021-08-30T04:50:00+10:00 |    0.2     | █████████████████████████  |
|      Water Temperature      |      °C      |          15         | 2021-08-30T04:45:00+10:00 |   25.346   | ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁  |
|      Water Temperature      |      °C      |          15         | 2021-08-30T04:45:00+10:00 |   25.323   | ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂  |
|      Water Temperature      |      °C      |          15         | 2021-08-30T04:45:00+10:00 |   25.347   | ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂  |
|        Wind Direction       |   dir deg    |          10         | 2021-08-30T04:50:00+10:00 |   156.8    | ▃▂▂▂▁▂▁▂▂▁▃▃▃▁▂▂▃▃▄▂▃▅▅▅▅  |
|      Wind Speed Average     |     km/h     |          10         | 2021-08-30T04:50:00+10:00 |  28.4004   | ▄▇▇▆▆▆█▇▇▇▆▆▆▆▆▅▅▆▆▆▆▅▆▅▆  |
|      Wind Speed Maximum     |     km/h     |          10         | 2021-08-30T04:50:00+10:00 |   33.48    | ▄▆▇▅█▆▇▇▆▆▆▅▆▆▆▅▄▅▆▅▇▆▅▄▆  |
|      Wind Speed Minimum     |     km/h     |          10         | 2021-08-30T04:50:00+10:00 |    21.6    | ▄▇▆▅▂▆█▇▆▇▅▆▆▆▆▅▅▆▆▅▆▅▆▆▅  |
+-----------------------------+--------------+---------------------+---------------------------+------------+----------------------------+

```