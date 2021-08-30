# WeatherStationsQC

Python and R functions to explore and perform quality control of data from AIMS weather stations

For the QC protocols, a JSON template for threshold values is drafted. Threshold values need to be read and passed to the functions.

# Python Code

## `stationID.py`

Get the station ID. The ID is the argument to be passed to the python function. Just run this as your first option

Example:

```
python stationID.py 
+-------------------------+------------+-----------------------------------------------------------------------------+
|       Station Name      | Station ID |                                 Metadata url                                |
+-------------------------+------------+-----------------------------------------------------------------------------+
| Agincourt Reef Number 3 |     1      | https://apps.aims.gov.au/metadata/view/5ee39300-4ade-11dc-8f56-00008a07204e |
|    Cape Bowling Green   |     2      | https://apps.aims.gov.au/metadata/view/5f30a190-4ade-11dc-8f56-00008a07204e |
|      Cleveland Bay      |     3      | https://apps.aims.gov.au/metadata/view/82422310-5a9d-11dc-8d3c-00008a07204e |
|          Darwin         |    1092    | https://apps.aims.gov.au/metadata/view/9c7a97f2-a06a-446c-9712-c6e719da0d24 |
|       Davies Reef       |     4      | https://apps.aims.gov.au/metadata/view/5fc91100-4ade-11dc-8f56-00008a07204e |
|        Hardy Reef       |     6      | https://apps.aims.gov.au/metadata/view/603df2e0-4ade-11dc-8f56-00008a07204e |
|       Heron Island      |    130     | https://apps.aims.gov.au/metadata/view/aefce70d-0ca2-494a-a8f9-47499e2c7f6e |
|      Lizard Island      |    1166    | https://apps.aims.gov.au/metadata/view/efc69c33-528f-4853-99aa-74d73e0daffa |
|       Masig Island      |    2601    | https://apps.aims.gov.au/metadata/view/5e211d53-549b-4162-b67c-9c05c1897a7b |
|      Myrmidon Reef      |     7      | https://apps.aims.gov.au/metadata/view/60b0d8f0-4ade-11dc-8f56-00008a07204e |
|      Ningaloo Reef      |     8      | https://apps.aims.gov.au/metadata/view/06ea6230-55f3-11dc-8d3c-00008a07204e |
|       Square Rocks      |     5      | https://apps.aims.gov.au/metadata/view/1b1c2a50-4f9e-11dc-9c63-00008a07204e |
|     Thursday Island     |    921     | https://apps.aims.gov.au/metadata/view/911a0982-240e-4461-ac0c-107f6e59a355 |
|         Yongala         |    1165    | https://apps.aims.gov.au/metadata/view/88ef50ff-262e-49b5-90a1-70c3a570045d |
+-------------------------+------------+-----------------------------------------------------------------------------+

```

## `AIMSweather_status`

Current operation status of all weather stations

Example: 

```
 python AIMSweather_status.py 
+------+-------------------------+--------+---------------------------+--------------------------------------------------------------------------------+
|  ID  |         STATION         | STATUS |        LAST READING       | PARAMETERS                                                                     |
+------+-------------------------+--------+---------------------------+--------------------------------------------------------------------------------+
|  1   | Agincourt Reef Number 3 | ONLINE | 2021-08-30T16:40:00+10:00 | WindSpeedAverage, AirPressure, AirTemperature, WindDirection, WaterTemperature |
|  2   |    Cape Bowling Green   | ONLINE | 2021-08-30T16:40:00+10:00 | AirPressure, WindDirection, AirTemperature, WindSpeedAverage                   |
|  3   |      Cleveland Bay      | ONLINE | 2021-08-30T16:40:00+10:00 | WindDirection, AirTemperature, AirPressure, WaterTemperature, WindSpeedAverage |
| 1092 |          Darwin         | ONLINE | 2021-08-30T16:00:00+09:30 | AirTemperature, WindSpeedAverage, WindDirection, AirPressure, WaterTemperature |
|  4   |       Davies Reef       | ONLINE | 2021-08-30T16:40:00+10:00 | AirTemperature, WaterTemperature, WindDirection, WindSpeedAverage, AirPressure |
|  6   |        Hardy Reef       | ONLINE | 2021-08-30T16:40:00+10:00 | WindDirection, WaterTemperature, AirTemperature, AirPressure, WindSpeedAverage |
| 130  |       Heron Island      | ONLINE | 2021-08-30T16:40:00+10:00 | WaterTemperature, WindSpeedAverage, WindDirection, AirTemperature, AirPressure |
| 1166 |      Lizard Island      | ONLINE | 2021-08-30T16:40:00+10:00 | WindSpeedAverage, WindDirection, AirTemperature, AirPressure                   |
| 2601 |       Masig Island      | ONLINE | 2021-08-30T16:40:00+10:00 | AirPressure, AirTemperature, WaterTemperature, WindDirection, WindSpeedAverage |
|  7   |      Myrmidon Reef      | ONLINE | 2021-08-30T16:40:00+10:00 | AirTemperature, AirPressure, WindDirection, WindSpeedAverage, WaterTemperature |
|  8   |      Ningaloo Reef      | ONLINE | 2021-08-30T14:40:00+08:00 | AirTemperature, WindSpeedAverage, WindDirection, AirPressure                   |
|  5   |       Square Rocks      | ONLINE | 2021-08-30T16:40:00+10:00 | WaterTemperature, AirTemperature, AirPressure, WindDirection, WindSpeedAverage |
| 921  |     Thursday Island     | ONLINE | 2021-08-30T16:40:00+10:00 | AirPressure, AirTemperature, WindDirection, WindSpeedAverage                   |
| 1165 |         Yongala         | ONLINE | 2021-08-30T16:00:00+10:00 | AirPressure, AirTemperature, WindSpeedAverage, WindDirection, WaterTemperature |
+------+-------------------------+--------+---------------------------+--------------------------------------------------------------------------------+

```

## `WSsummary.py`

```
usage: WSsummary.py [-h] -site SITE [-noplot]

AIMS weather station summary: latest readings.

optional arguments:
  -h, --help  show this help message and exit
  -site SITE  site ID
  -noplot     do not plot the latest readings
```



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


# R Code

The R code is in the form of Rmarkdown notebooks. 