#! /usr/bin/env python3

import urllib.request
#import polymodule as pm

theurl = "http://www.msftncsi.com/ncsi.txt"
#  Old Polybar Version
#theupicon = " "
#thedownicon = " "
#theupcolor = pm.pycolors('color7')
#thedowncolor = pm.pycolors('color2')

# New Conky Version
theupicon = "${font Font Awesome 6 Free Solid:size=11}${color 009900} ${color 4F4F4F}${font} "
thedownicon = "$font Font Awesome 6 Free Solid:size=11}${color 990000} ${color 4f4f4f}{$font}"


therequest = urllib.request.Request(theurl)
try:
    theresponse = urllib.request.urlopen(therequest)
    #print("%{{F{}}} {}%{{F-}}".format(theupcolor,theupicon))
    print(theupicon)
except urllib.error.HTTPError as e:
    #print("%{{F{}}} {}%{{F-}}".format(thedowncolor,thedownicon))
    print(thedownicon)
except urllib.error.URLError as e:
    #print("%{{F{}}} {}%{{F-}}".format(thedowncolor,thedownicon))
    print(thedownicon)


