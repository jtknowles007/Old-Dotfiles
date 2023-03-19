#! /usr/bin/env python3 
import urllib.request
import netifaces

interface = 'enp3s0'
url = "http://www.msftncsi.com/ncsi.txt"
upicon = "<span color='green'></span>"
downicon = "<span color=''red'></span>"
def getipaddress(ifname):
    try:
        ip = netifaces.ifaddresses(ifname)[netifaces.AF_INET][0]['addr']
        return ip
    except:
        return '0.0.0.0'



def geturl(website):
    request = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(request)
        return upicon
    except urllib.error.HTTPError as e:
        return downicon
    except urllib.error.URLError as e:
        return downicon

print(" {} {}".format(getipaddress(interface),geturl(url)))

