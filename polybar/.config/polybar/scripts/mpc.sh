#! /usr/bin/env bash
if ! mpc >/dev/null 2>&1; then
    echo MPC Offline
    exit 1
elif mpc status | grep -q playing; then
    (mpc current | zscroll -l 30 -d 0.3) &
else
    echo Not Playing
fi

mpc idle >/dev/null
