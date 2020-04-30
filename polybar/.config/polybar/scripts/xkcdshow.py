#! /usr/bin/env python3

import webbrowser

xkcdfile = open('xkcd.txt','r')
url = xkcdfile.read()
xkcdfile.close()
webbrowser.open(url)
