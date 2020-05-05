#! /usr/bin/env bash
if ! mpc >/dev/null 2>&1; then
    echo MPC Offline
    exit 1
elif mpc status | grep -q playing; then
    (mpc --format "%album% ** %title%" current | zscroll -l 20 -b " " -p " ** " --delay 0.3 --update-check true "mpc --format '%album% ** %title%' current ") &
else
    echo Not Playing
fi
mpc idle >/dev/null
