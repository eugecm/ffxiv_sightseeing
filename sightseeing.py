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
    eorzea_timestamp = now.timestamp() * 20.571428571428573;
    weather_data = weather_provider.weather_at(now.timestamp())

    # TODO: This is naive. Can be made faster
    available_vistas = []
    for location, weather in weather_data.items():
        for vista in vistas:
            if vista.location != location:
                continue
            if not vista.is_available(weather, eorzea_timestamp):
                continue
            available_vistas.append(vista)

    print('Go to https://ffxiv.consolegameswiki.com/wiki/Sightseeing_Log')
    eorzea_time = datetime.fromtimestamp(eorzea_timestamp)
    print('It is', eorzea_time, '(Eorzea time)')

    if len(available_vistas) == 0:
        print('No vistas are available now. Try again later')
        return

    available_vistas.sort(key=lambda v: int(v.entry))
    print('The following vistas are available now:\n\n')
    print('ENTRY', 'TIME', 'LOCATION', 'WEATHER', sep='\t')
    for vista in available_vistas:
        print(vista.entry, vista.time, vista.location, vista.weather, sep='\t')

if __name__ == '__main__':
    run()
