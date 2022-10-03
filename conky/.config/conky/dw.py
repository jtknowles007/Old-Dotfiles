#! /usr/bin/env python3

import getjson as pm
from credentials import darkkey

latitude = 40.0545
longitude = -85.6743

# Find local weather
weatherurl = "https://api.darksky.net/forecast/{}/{},{}".format(darkkey,latitude,longitude)
weatherdata = pm.getjson(weatherurl)

# Gather data elements from weather report that we're interested in seeing
current = round(weatherdata['currently']['temperature'],1)
symbol = "°F"
condition = weatherdata['currently']['summary']

# Get the weather icon code and match it to the corresponding weather font
# unicode characters from https://erikflowers.github.io/weather-icons/
icon = weatherdata['currently']['icon']
icondefault = ""
icondict = {
    "clear-day":"${color FFFF00} ${color 4F4F4F}",
    "clear-night":"${color BBBBBB} ${color 4F4F4F}",
    "partly-cloudy-day":"",
    "partly-cloudy-night":"",
    "rain":"${color 3399FF} ${color 4F4F4F}",
    "sleet":"",
    "snow":"${color FFFFFF} ${color 4F4F4F}",
    "wind":"",
    "fog":""
    }

# Output Weather 
print("${{font Weather Icons:size=20}}{}${{font}} {}{}".format(icondict.get(icon,icondefault),current,symbol))
