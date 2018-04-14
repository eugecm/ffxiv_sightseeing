import argparse
from datetime import datetime, timedelta

from vista import load_vistas
from weather import WeatherProvider

parser = argparse.ArgumentParser(description='Find out which vistas are available for the sightseeing log')
parser.add_argument('--weatherdata', type=str, default='weather.json')
parser.add_argument('--vistasdata', type=str, default='vistas.json')
parser.add_argument('--utcdiff', type=int, default=0)

def run():
    args = parser.parse_args()
    weather_provider = WeatherProvider(args.weatherdata)
    vistas = load_vistas(args.vistasdata)

    now = datetime.utcnow() + timedelta(hours=args.utcdiff)
    now = now.replace(second=0, microsecond=0)

    print('Go to https://ffxiv.consolegameswiki.com/wiki/Sightseeing_Log')

    print('\nThe following vistas will be available:\n')
    print('REAL_TIME', 'ENTRY', 'TIME', 'LOCATION', 'WEATHER', sep='\t')

    to_see = {vista.entry for vista in vistas}
    tick = 0
    while len(to_see) > 0:
        then = (now.timestamp() + (tick * 3 * 60))
        eorzea_timestamp = then * 20.571428571428573;
        weather_data = weather_provider.weather_at(then)
        for location, weather in weather_data.items():
            for vista in vistas:
                if vista.entry not in to_see:
                    continue
                if vista.location != location:
                    continue
                if not vista.is_available(weather, eorzea_timestamp):
                    continue
                print(datetime.fromtimestamp(then), vista.entry, vista.time, vista.location, vista.weather, sep='\t')
                to_see.remove(vista.entry)
        tick += 1


if __name__ == '__main__':
    run()
