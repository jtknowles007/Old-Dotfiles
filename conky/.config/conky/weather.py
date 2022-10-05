#! /usr/bin/env python3

import getjson as pm
from credentials import openweather

latitude = 40.05
longitude = -85.67

# Find local weather
weatherurl = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=imperial&appid={}".format(latitude,longitude,openweather)
weatherdata = pm.getjson(weatherurl)

# Gather data elements from weather report that we're interested in seeing
current = round(weatherdata['main']['temp'],0)
high = round(weatherdata['main']['temp_max'],0)
low = round(weatherdata['main']['temp_min'],0)
symbol = "°F"
condition = weatherdata['weather'][0]['description'].title()
path = "~/Dotfiles/conky/.config/conky/weatherimages/"
icon = weatherdata['weather'][0]['icon']
filetype = ".png"
iconpath = path + icon + filetype
# Output Weather 
print("${{image {} -s 50x50}} ${{offset 50}}${{voffset 20}}{}${{offset 25}}Currently:{}{} ${{offset 25}}Low:{}{}${{offset 10}}High:{}{}".format(iconpath,condition,current,symbol,low,symbol,high,symbol))
