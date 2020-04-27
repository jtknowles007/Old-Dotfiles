#! /usr/bin/env python3

import tkinter as tk
import polymodule as pm
from tkinter import font
from credentials import darkkey
from credentials import locationiqkey
from collections import OrderedDict





symbol = "°F"
# Find Latitude and Longitude based on URL
ipurl = "https://ipapi.co/json/"
ipdata = pm.getjson(ipurl)
lat = ipdata['latitude']
long = ipdata['longitude']

#Find Location and Weather
locationurl = "https://us1.locationiq.com/v1/search.php?key={}&q={},{}&format=json&statecode=1&addressdetails=1".format(locationiqkey,lat,long)
weatherurl = "https://api.darksky.net/forecast/{}/{},{}".format(darkkey,lat,long)
locationdata = pm.getjson(locationurl)
weatherdata = pm.getjson(weatherurl)

city = locationdata[0]['address']['city']
state = locationdata[0]['address']['state_code']
state = state.upper()
citystate = "{}, {}".format(city,state)
current = str(round(weatherdata['currently']['temperature'],1))+symbol
feelslike = str(round(weatherdata['currently']['apparentTemperature'],1))+symbol
high = str(round(weatherdata['daily']['data'][0]['temperatureHigh'],1))+symbol
low = str(round(weatherdata['daily']['data'][0]['temperatureLow'],1))+symbol
humidity = str(round(weatherdata['currently']['humidity']*100,1))+"%"
cover = str(round(weatherdata['currently']['cloudCover']*100,1))+"%"
now = weatherdata['currently']['summary']
summary = weatherdata['hourly']['summary']
icon = weatherdata['currently']['icon']
wsummary = weatherdata['daily']['summary']
windowtitle = "DarkSkyWeather"
imagepath = "~/Dotfiles/polybar/.config/polybar/images/"
imageicon = "{}{}.png".format(imagepath,icon)
canvaswidth= 250
canvasheight = 300
textfg = "dark slate gray"
buttonbg = "LightSteelBlue3"
buttonfg = "gray1"
canvasbg = "white"

weatherdict = OrderedDict({
    0:("Weather for",citystate),
    1:("Temperature",current),
    2:("Feels Like",feelslike),
    3:("High",high),
    4:("Low",low),
    5:("Humidity",humidity),
    6:("Cloud Cover",cover),
    7:("Forecast",wsummary),
    })

# Create the main Tkinter window and canvas
window = tk.Tk(screenName=":0")
window.title(windowtitle)
canvas = tk.Canvas(
    window,
    width = canvaswidth,
    height = canvasheight,
    bg = canvasbg
    )
canvas.pack()

# Set the background image based on current weather conditions
image = tk.PhotoImage(file=imageicon)
canvas.create_image(0,0, image = image, anchor = 'nw')

# Iterate throught the weather data we want displayed and output to the window
for i,j in weatherdict.items():
    key = weatherdict[i][0]
    val = weatherdict[i][-1]
    canvas.create_text(
    10,20*i+10,
    anchor="nw",
    text = "{}: {}".format(key,val),
    fill=textfg,
    font=("Helvetica", 12),
    width=230
    )
    canvas.update

# Create and display close button
button = tk.Button(
    window, 
    text="Quit",
    command=window.destroy,
    bg=buttonbg,
    fg=buttonfg
    )
canvas.create_window(canvaswidth/2,canvasheight*0.90,window=button)

# Display the main window
window.mainloop()
