#!/usr/bin/env python3
# volume.py
# A volume indicator script for i3bar-Conky
# Copyright (c) 2017 John T. Knowles
#
# The following is a derivative of battery.py by James Murphy,
# which is licensed GPLv2.  This code is therefore also licensed under
# the terms of the GNU Public License, version 2.

from subprocess import check_output

status = check_output(['amixer'], universal_newlines=True)

if not status:
    # No sound mixer found
    fulltext = " "
    percentleft = 100
else:
    state = status.split(" ")[30]
    state = state[1:-2]
    state = int(state)

    fulltext = ""

    def VolumeIcon(percent):
        if percent < 10:
            return ""
        if percent < 50:
            return ""
        return ""

    form =  "{} {}"
    fulltext = form.format(VolumeIcon(state), state)
    fulltext += "%"
print(fulltext)
