#!/usr/bin/env bash
# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

MONITOR=DVI-I-1 polybar primary_bar &
MONITOR=HDMI-1 polybar secondary_bar &


