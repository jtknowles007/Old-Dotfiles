#!/usr/bin/env python3
# battery.py
# A battery indicator script for i3bar-Conky
# Copyright (c) 2017 John T. Knowles
#
# The following is a derivative of battery.py by James Murphy,
# which is licensed GPLv2.  This code is teherefore also licensed under
# the terms of the GNU Public License, version 2.

from subprocess import check_output

status = check_output(['acpi'], universal_newlines=True)

if not status:
    # No battery found
    fulltext = " "
    percentleft = 100
else:
    state = status.split(": ")[1].split(", ")[0]
    commasplitstatus = status.split(", ")
    percentleft = int(commasplitstatus[1].rstrip("%\n"))

    # stands for charging
    FA_LIGHTNING = "" 

    # stands for plugged in
    FA_PLUG = ""

    fulltext = ""
    timeleft = ""

    def BatteryIcon(percent):
        if percent < 10:
            return " "
        if percent < 35:
            return " "
        if percent < 65:
            return " "
        if percent <80:
            return " "
        return " "

    form =  "{}{}"
    if state == "Discharging":
        time = commasplitstatus[-1].split()[0]
        time = ":".join(time.split(":")[0:2])
        timeleft = " [{}]".format(time)
        fulltext += form.format(BatteryIcon(percentleft), timeleft)
    elif state == "Full":
        fulltext = FA_PLUG
    elif state == "Unknown":
        fulltext = ""
    else:
        fulltext = form.format(FA_LIGHTNING, percentleft)
        fulltext += "%"
print(fulltext)
