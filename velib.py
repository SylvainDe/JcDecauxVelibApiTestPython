#! /usr/bin/python3
# vim: set tabstop=4 shiftwidth=4 expandtab :

import os
import requests
import datetime
import time

CONTRACTS_URL = "https://api.jcdecaux.com/vls/v1/contracts?apiKey={0}"
STATIONS_URL = "https://api.jcdecaux.com/vls/v1/stations?contract={1}&apiKey={0}"
STATION_URL = "https://api.jcdecaux.com/vls/v1/stations/{1}?contract={2}&apiKey={0}"
STATIONS = [19027, 19036, 19113, 19026]
DATEFORMAT = "%Y-%m-%d_%H-%M-%S"

api_key = os.getenv('API_KEY', None)
if api_key is None:
    raise Exception("API_KEY is not provided in the environment")
print(api_key)
while True:
    for station in STATIONS:
        filename = "%d.txt" % station
        url = STATION_URL.format(api_key, station, 'Paris')
        # print(url)
        response = requests.get(url)
        # print(response.status_code)
        json = response.json()
        # print(json.keys())
        now = datetime.datetime.now()
        now_str = now.strftime(DATEFORMAT)
        last_up = datetime.datetime.fromtimestamp(json['last_update']/1000)
        last_up_str = last_up.strftime(DATEFORMAT)
        log = "%s STATION:%d LAST_UPDATE:%s BIKES:%d STANDS:%d TOTAL:%d" % (now_str, json['number'], last_up_str, json['available_bikes'], json['available_bike_stands'], json['bike_stands'])
        print(log)
        with open(filename, 'a') as f:
            f.write(log + "\n")
        time.sleep(20)
