#! /usr/bin/env python3

import requests
from credentials import openweatherkey

latitude = 40.1079
longitude = -85.6782
weatherurl = "https://api.openweathermap.org/data/2.5/weather"
params = {
    'units':'imperial',
    'lat':latitude,
    'lon':longitude,
    'appid':openweatherkey
}

try:
    response = requests.get(weatherurl, params=params)
except requests.exceptions.Timeout:
    print("Time Out")
except requests.exceptions.TooManyRedirects:
    print("Too Many Redirects")
except requests.exceptions.RequestException:
    print("Error Occured")

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
