#! /usr/bin/env python3

import json
import requests

#Read Pywal colors
filepath = "/home/john/.cache/wal/colors.json"
with open(filepath, encoding='utf-8-sig') as colorjson:
    text = colorjson.read()
    json_data = json.loads(text)
color6 = json_data['colors']['color6']
color10 = json_data['colors']['color10']
color13 = json_data['colors']['color13']

#Gather COVID-9 Data
covidurl = "https://covid19api.io/api/v1/CasesInAllUSStates"
covid = requests.get(covidurl)
coviddata = json.loads(covid.text)

totalcases = coviddata['data'][0]['table'][0]['TotalCases']
totaldeaths = coviddata['data'][0]['table'][0]['TotalDeaths']

#Display COVID-19 data in Polybar
print("%{{F{} T4}}若%{{F- T-}} US: %{{F{}}} %{{F-}}{} %{{F{}}} %{{F-}} {}".format(color6,color13,totalcases,color10,totaldeaths))
