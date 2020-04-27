#! /usr/bin/env python3

import json
import requests
from credentials import key

# Find out where we are based on external IP address
ipurl = "https://ipapi.co/json/"
ip = requests.get(ipurl)
ipdata = json.loads(ip.text)

# Gather data to pass to weather api
city = ipdata['city']
country = ipdata['country']
units = "imperial"
if city == "Anderson":
    cityid = "4917592"
    weatherurl = "http://api.openweathermap.org/data/2.5/weather?APPID={}&id={}&units={}".format(key,cityid,units)
else:
    weatherurl = "http://api.openweathermap.org/data/2.5/weather?APPID={}&q={},{}&units={}".format(key,city,country,units)
# Find out the local weather
weather = requests.get(weatherurl)
weatherdata = json.loads(weather.text)

# Gather data elements from weather report that we're interested in seeing
location = weatherdata['name']
current = round(weatherdata['main']['temp'],1)
symbol = ""
condition = weatherdata['weather'][0]['description']

# Get the weather icon code and match it to the corresponding weather font
# unicode character from https://erikflowers.github.io/weather-icons/
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
    "09d":"",
    "09n":"",
    "10d":"",
    "10n":"",
    "11d":"",
    "11n":"",
    "13d":"",
    "13n":"",
    "50d":"",
    "50n":""
    }

# Display weather in Polybar
print("{}: {}{}, {} {}".format(location,current,symbol,condition.title(),icondict.get(icon,icondefault)))


