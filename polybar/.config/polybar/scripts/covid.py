#! /usr/bin/env python3

# Adapted from HauctoPuce's Polybar Covid Tracker
# github.com/HauctoPuce/polybar_covid_tracker

import json
import requests
import polymodule as pm

#Assign Pywal colors
virusiconcolor = pm.pycolors('color6')
positivecolor = pm.pycolors('color13')
deathscolor = pm.pycolors('color10')

#Gather COVID-9 Data
covidurl = "https://covid19api.io/api/v1/CasesInAllUSStates"
covid = requests.get(covidurl)
coviddata = json.loads(covid.text)

totalcases = coviddata['data'][0]['table'][0]['TotalCases']
totaldeaths = coviddata['data'][0]['table'][0]['TotalDeaths']

#Display COVID-19 data in Polybar
print("%{{F{} T4}}若%{{F- T-}} US: %{{F{}}} %{{F-}}{} %{{F{}}} %{{F-}} {}".format(virusiconcolor,positivecolor,totalcases,deathscolor,totaldeaths))
