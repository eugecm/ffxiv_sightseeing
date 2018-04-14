# ffxiv_sightseeing
Helper script to list when FFXIV sightseeing vistas will be available. Requires Python 3

# How to run:
    python sightseeing.py --utcdiff 5
    Go to https://ffxiv.consolegameswiki.com/wiki/Sightseeing_Log
    
    The following vistas will be available:

    REAL_TIME	ENTRY	TIME	LOCATION	WEATHER
    2018-04-14 08:14:00	24	8AM-12PM	Eastern La Noscea	Fair/Clear
    2018-04-14 08:14:00	1	8AM-12PM	Limsa Lominsa	Fair/Clear
    2018-04-14 08:14:00	37	8AM-12PM	Gridania	Fair/Clear
    2018-04-14 08:14:00	12	8AM-12PM	East Shroud	Fair/Clear
    2018-04-14 08:14:00	45	8AM-12PM	South Shroud	Fair/Clear
    ....

`--utcdiff` can be used to indicate the timezone. For example `--utcdiff 1` for British Summer Time
Go to https://ffxiv.consolegameswiki.com/wiki/Sightseeing_Log
