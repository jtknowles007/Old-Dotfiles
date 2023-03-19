#! /usr/bin/env python3

import getjson as pm
from credentials import darkkey


# Find Latitude and Longitude based on IP
ipurl = "https://ipapi.co/json/"
ipdata = pm.getjson(ipurl)
latitude = 40.1079
longitude = -85.6782

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
    "clear-day":"",
    "clear-night":"",
    "partly-cloudy-day":"",
    "partly-cloudy-night":"",
    "rain":"",
    "sleet":"",
    "snow":"",
    "wind":"",
    "fog":""
    }

# Output Weather 
print(" {}{} <span font='Weather Icons'>{}</span>".format(current, symbol, icondict.get(icon,icondefault)))
