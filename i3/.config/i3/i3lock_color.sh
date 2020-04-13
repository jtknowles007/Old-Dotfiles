#!/bin/bash
. ~/.cache/wal/colors.sh

a="ff"
color0a="$color0$a"
color1a="$color1$a"
color2a="$color2$a"
color3a="$color3$a"
color4a="$color4$a"
color5a="$color5$a"
color6a="$color6$a"
color7a="$color7$a"
color8a="$color8$a"

i3lock \
-i $wallpaper \
--insidevercolor=$color5a   \
--ringvercolor=$color4a     \
\
--insidewrongcolor=$color2a \
--ringwrongcolor=$color2a   \
\
--insidecolor=$color1a      \
--ringcolor=$color4a \
--linecolor=$color2a        \
--separatorcolor=$color0a   \
\
--textcolor=$color0a        \
--timecolor=$color0a        \
--datecolor=$color0a        \
--layoutcolor=$color0a      \
--keyhlcolor=$color2a       \
--bshlcolor=$color2a        \
\
--screen 0            \
--blur 5              \
--clock               \
--indicator           \
--timestr="%I:%M %P"  \
--datestr="%h %d, %Y" \

