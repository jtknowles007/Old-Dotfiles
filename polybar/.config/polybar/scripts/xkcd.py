#! /usr/bin/env python3

import polymodule as pm
color = pm.pycolors('color6')

url = "https://xkcd.com/info.0.json"
xkcd = pm.getjson(url)
title = xkcd['safe_title']
link = xkcd['img']

xkcdfile = open('xkcd.txt', 'w')
xkcdfile.write(link)
xkcdfile.close()

print("%{{F{} T4}}%{{F- T-}}xkcd: {}".format(color,title))
