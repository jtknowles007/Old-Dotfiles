#! /usr/bin/env python3
import sys
import wget
import PySimpleGUI as sg
import polymodule as pm
color = pm.pycolors('color6')

url = "https://xkcd.com/info.0.json"
xkcd = pm.getjson(url)
title = xkcd['safe_title']
image = xkcd['img']

if len(sys.argv) > 1:
    imagefile = wget.download(image,'../images/xkcd.png')
    sg.theme('DarkAmber')
    layout = [[sg.Image(imagefile)],[sg.Button('Close')]]

    # To specify exact monitor where this window should be place, see i3 config file.
    window = sg.Window('xkcd_comic', layout, no_titlebar=True, location=(700,32))

    while True:
        event, values = window.read()
        if event in (None,'Close'):
            break
    window.close()
else:   
    print("%{{F{} T4}}%{{F- T-}}xkcd: {}".format(color,title))
