#!/usr/bin/env bash

WALLDIR="/home/john/Pictures/Wallpaper/"

BACKEND="colorthief"
THEME=('Woodgrain Muted' 'Abstract_WoodgrainMutedColors.jpg')
THEME+=('Bokeh' 'Abstract_Bokeh.jpg')
THEME+=('Station Ruins' 'Abandoned_StationRuins.jpg')

ARR=("${THEME[0]}")
ARR+=("${THEME[2]}")
ARR+=("${THEME[4]}")

CHOICE=$(printf '%s\n' "${ARR[@]}" | rofi -dmenu -config /home/john/.config/polybar/ThemeChooserRofiMenu.config -p "Theme Chooser")

if [ "$CHOICE" = "${THEME[0]}" ]; then
    wal --backend "$BACKEND" -i "$WALLDIR${THEME[1]}"
    exit 0
fi

if [ "$CHOICE" = "${THEME[2]}" ]; then
    wal --backend "$BACKEND" -i "$WALLDIR${THEME[3]}"
    exit 0
fi

if [ "$CHOICE" = "${THEME[4]}" ]; then
    wal --backend "$BACKEND" -i "$WALLDIR${THEME[5]}"
    exit 0
fi
