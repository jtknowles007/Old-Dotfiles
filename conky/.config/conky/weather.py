#! /usr/bin/env python3

import getjson as pm
from credentials import openweather

# Variables
latitude = 40.05 # Lat of Anderson IN
longitude = -85.67 # Lon of Anderson IN
symbol = "°F"
symbol2 = "%"
path = "~/Dotfiles/conky/.config/conky/weatherimages/"
filetype = ".png"

# Get current weather from OpenWeather and extract JSON data
weatherurl = ("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}" \
              "&units=imperial&appid={}".format(latitude,longitude,openweather))
weatherdata = pm.getjson(weatherurl)

# Gather data elements from weather report that we're interested in displaying
current = round(weatherdata['main']['temp'],0)
feelslike = round(weatherdata['main']['feels_like'],0)
humidity = round(weatherdata['main']['humidity'],0)
condition = weatherdata['weather'][0]['description'].title()
icon = weatherdata['weather'][0]['icon']

#Built path to the icons
iconpath = path + icon + filetype

# Output weather in Conky format
print("${{image {} -p 0,0 -s 50x50}} ${{offset 50}}${{voffset 20}}{}${{offset 25}}" \
      "Currently:{}{} ${{offset 25}}Feels Like:{}{} ${{offset 25}}Humidity:{}{}" \
      .format(iconpath,condition,current,symbol,feelslike,symbol,humidity,symbol2))
