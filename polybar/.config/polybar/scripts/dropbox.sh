#!/usr/bin/env bash
# Adapted from "Custom Menu Using Rofi + Polybar" at https://youtu.be/gmQMhU-hw3s
# Required some modification based around calling the dropbox CLI tool.
ST=$(dropbox status)

ARR=()
ARR+=("Status: $ST")
ARR+=("  Start")
ARR+=("  Stop")
ARR+=("Proxy:")
ARR+=("  None")
ARR+=("  Auto")
ARR+=("  Proxy")



CHOICE=$(printf '%s\n' "${ARR[@]}" | rofi -m primary -dmenu -config /home/john/.config/polybar/DropboxRofiMenu.config -p "Dropbox: ")

if [ "$CHOICE" = "  Start" ]; then
    dropbox start
    exit 0
fi

if [ "$CHOICE" = "  Stop" ]; then
    dropbox stop
    exit 0
fi

if [ "$CHOICE" = "  None" ]; then
    dropbox proxy none
    exit 0
fi

if [ "$CHOICE" = "  Auto" ]; then
    dropbox proxy auto
    exit 0
fi

if [ "$CHOICE" = "  Proxy" ]; then
    dropbox proxy manual 0.0.0.0 username password
    exit 0
fi
