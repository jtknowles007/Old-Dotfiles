#! /usr/bin/env python3

import json
import requests
import webbrowser

ipurl = "https://ipapi.co/json/"
weatherbase = "https://openweathermap.org"
ip = requests.get(ipurl)
ipdata = json.loads(ip.text)

city = ipdata['city']
country = ipdata['country']
if city =="Anderson":
    cityid = "/city/4917592"
else:
    cityid = "/find?q={}%2C+{}".format(city,country)

weatherurl = weatherbase + cityid
webbrowser.open(weatherurl,new=1,autoraise=True)

