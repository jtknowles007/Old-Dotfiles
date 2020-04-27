#! /usr/bin/env python3

"""Polymodule.py: Common functions for polybar scripts."""

#############################
# Imports                   #
#############################

import json
import requests

#############################
# Functions                 #
#############################

def pycolors(color):
    """
    Get color values from Pywal.
    
    Return the HEX (#RRGGBB) color value of requested color number from Pywal json file.

    Parameters:
    arg1(string): Input 'colorN' where N = 0 through 15.
    
    Returns:
    colorvalue(string): HEX value of requested color.
    """
    pywaljson = "/home/john/.cache/wal/colors.json"
    with open(pywaljson,'r') as pwc:
        pywalcolor = json.loads(pwc.read())
    colorvalue = pywalcolor['colors'][color]
    return colorvalue

def getjson(url):
    """
    Get JSON data from web.
    
    Return JSON data from url passed to the function.

    Parameters:
    arg1(string): URL of JSON file.
    
    Returns:
    jsondata(string): Dict of JSON data returned from URL.
    """    
    getdata = requests.get(url)
    jsondata = json.loads(getdata.text)
    return jsondata
