#! /usr/bin/env python3

import json
import requests
import polymodule as pm
from credentials import darkkey

#Assign colors from Pywal
weathericoncolor = pm.pycolors('color6')

# Find out where we are based on external IP address
ipurl = "https://ipapi.co/json/"
ip = requests.get(ipurl)
ipdata = json.loads(ip.text)

# Gather data to pass to weather api
lat = ipdata['latitude']
long = ipdata['longitude']
weatherurl = "https://api.darksky.net/forecast/{}/{},{}".format(darkkey,lat,long)

# Find out the local weather
weather = requests.get(weatherurl)
weatherdata = json.loads(weather.text)

# Gather data elements from weather report that we're interested in seeing
current = round(weatherdata['currently']['temperature'],1)
symbol = "°F"
condition = weatherdata['currently']['summary']

# Get the weather icon code and match it to the corresponding weather font
# unicode character from https://erikflowers.github.io/weather-icons/
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

# Display weather in Polybar 
print("%{{F{}}} {}%{{F-}} {}{}".format(weathericoncolor,icondict.get(icon,icondefault),current,symbol))
