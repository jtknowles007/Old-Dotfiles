#! /usr/bin/env python3

import json

#############################
# Get Colors from Pywal     #
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
