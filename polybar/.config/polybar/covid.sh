#! /usr/bin/zsh

# ===================================================================== #
#  file: covid_tracker.sh                                               #
#  Fetch coronavirus progression data from the coronavirus-tracker API  #
#  https://github.com/ExpDev07/coronavirus-tracker-api                  #
# ===================================================================== #

color6=$(polybar --dump=color6 colorbar)
color10=$(polybar --dump=color10 colorbar)
color13=$(polybar --dump=color13 colorbar)
color14=$(polybar --dump=color14 colorbar)
URL="https://coronavirus-tracker-api.herokuapp.com/v2/locations?source=jhu&country_code=US"
res=$(curl -sf "$URL")

if [ -z "$res" ]; then
    echo " Impossible to fetch data. "
    return 1
fi

nb_confirmed=$(jq '.["latest"]["confirmed"]' <<< $res)
nb_death=$(jq '.["latest"]["deaths"]' <<< $res)
nb_recovered=$(jq '.["latest"]["recovered"]' <<< $res)

echo "%{F$color6 T4}若%{F- T-} US: %{F$color13}%{F-} $nb_confirmed %{F$color10}%{F-} $nb_death" | sed ':a;s/\B[0-9]\{3\}\>/,&/;ta'
