#! /usr/bin/env python3
import time

uptime = time.clock_gettime(time.CLOCK_BOOTTIME)
intervals = (
    ('weeks',604800),
    ('days',86400),
    ('hours',3600),
    ('minutes',60),
    ('seconds',1),
)

def secondstotext(secs):
    days = int(secs//86400)
    hours = int((secs -days*86400)//3600)
    minutes = int((secs - days*86400 - hours*3600)//60)

    result = ("{}d ".format(days) if days else "0d ") + \
            ("{}h ".format(hours) if hours else "0h ") +\
            ("{}m".format(minutes) if minutes else "0m")
    return result

print(" {}".format(secondstotext(uptime)))

