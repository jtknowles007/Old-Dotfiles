#! /usr/bin/env python3

# Adapted from HauctoPuce's Polybar Covid Tracker
# github.com/HauctoPuce/polybar_covid_tracker

import json
import requests
import polymodule as pm
from recursive_json import extract_values

#Assign Pywal colors
virusiconcolor = pm.pycolors('color6')
positivecolor = pm.pycolors('color13')
deathscolor = pm.pycolors('color10')

#Gather COVID-9 Data
covidurl = "https://api.covid19api.com/summary"
covid = requests.get(covidurl)
coviddata = json.loads(covid.text)

#Extract data into lists
country = extract_values(coviddata,'CountryCode')
cases = extract_values(coviddata,'TotalConfirmed')
deaths = extract_values(coviddata,'TotalDeaths')

#Remove worldwide total cases and deaths from respective lists
cases = cases[1:]
deaths = deaths[1:]

#Extract US data
usindex = country.index('US')
uscases = cases[usindex]
usdeaths = deaths[usindex]

#Display COVID-19 data in Polybar
print("%{{F{} T4}}若%{{F- T-}} US: %{{F{}}} %{{F-}}{:,} %{{F{}}} %{{F-}}{:,}".format(virusiconcolor,positivecolor,uscases,deathscolor,usdeaths))
