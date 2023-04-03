#! /usr/bin/env python3

import requests
from credentials import openweatherkey

weatherurl = "https://api.openweathermap.org/data/2.5/weather"
units="imperial"
latitude = 40.1079
longitude = -85.6782

def getcurrentweather(theurl,theunits,thelat,thelong,thekey):
    params = {
        'units':theunits,
        'lat':thelat,
        'lon':thelong,
        'appid':thekey
    }

    try:
        response = requests.get(theurl, params=params)
    except:
        print("Error Occurred")
        return

    weatherdata = response.json()
    current = round(weatherdata['main']['temp'],1)
    symbol = "°F"
    icon = weatherdata['weather'][0]['icon']
    icondefault = ""
    icondict = {
        "01d":"",
        "01n":"",
        "02d":"",
        "02n":"",
        "03d":"",
        "03n":"",
        "04d":"",
        "04n":"",
        "09d":"",
        "09n":"",
        "10d":"",
        "10n":"",
        "11d":"",
        "11n":"",
        "13d":"",
        "13n":"",
        "50d":"",
        "50n":""
        }

    print(" {}{} <span font='Weather Icons'>{}</span>".format(current, symbol, icondict.get(icon,icondefault)))

if __name__ == "__main__":
    getcurrentweather(weatherurl,units,latitude,longitude,openweatherkey)
