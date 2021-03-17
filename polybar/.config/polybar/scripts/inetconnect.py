#! /usr/bin/env python3


import urllib.request
import polymodule as pm

theurl = "http://www.msftncsi.com/ncsi.txt"
theupicon = ""
thedownicon = ""
theupcolor = pm.pycolors('color6')
thedowncolor = pm.pycolors('color2')

therequest = urllib.request.Request(theurl)
try:
    theresponse = urllib.request.urlopen(therequest)
    print("%{{F{}}} {}%{{F-}}".format(theupcolor,theupicon))
except urllib.error.HTTPError as e:
    print("%{{F{}}} {}%{{F-}}".format(thedowncolor,thedownicon))
except urllib.error.URLError as e:
    print("%{{F{}}} {}%{{F-}}".format(thedowncolor,thedownicon))


