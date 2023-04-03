#! /usr/bin/env python3

import getjson as pm
from credentials import openweatherkey

latitude = 40.1079
longitude = -85.6782

# Find local weather
weatherurl = "https://api.openweathermap.org/data/2.5/weather?units=imperial&lat={}&lon={}&appid={}".format(latitude,longitude,openweatherkey)
weatherdata = pm.getjson(weatherurl)
current = round(weatherdata['main']['temp'],1)
symbol = "°F"
condition = weatherdata['weather'][0]['description']
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
