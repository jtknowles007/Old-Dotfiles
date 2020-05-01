#! /usr/bin/env python3

import PySimpleGUI as sg
import wget

import polymodule as pm

url = 'https://xkcd.com/info.0.json'
xkcd = pm.getjson(url)
image = xkcd['img']

imagefile = wget.download(image)
sg.theme('DarkAmber')
layout = [[sg.Image(imagefile)],[sg.Button('Close')]]
window = sg.Window('xkcd_comic', layout, no_titlebar=True, location=(700,32))

while True:
    event, values = window.read()
    if event in (None,'Close'):
        break
window.close()
