#! /usr/bin/env python3


import urllib.request

theurl = "http://www.msftncsi.com/ncsi.txt"
therequest = urllib.request.Request(theurl)
try:
    theresponse = urllib.request.urlopen(therequest)
    print("")
except urllib.error.HTTPError as e:
    print("")
except urllib.error.URLError as e:
    print("")


