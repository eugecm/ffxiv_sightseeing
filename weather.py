import json
import time
from datetime import datetime, timedelta

class WeatherProvider:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.weather_data = json.load(f)

    def weather_at(self, timestamp):
        # Calculate zone weather at timestamp
        zone_weather = {}
        target = self._calculate_weather_forecast_target(timestamp)
        for zone, zone_weathers in self.weather_data['zoneWeather'].items():
            zone_rates = self.weather_data['zoneRates'][zone]
            current_weather = None
            for weather, rate in zip(zone_weathers, zone_rates):
                if target < rate:
                    current_weather = weather
                    break
            else:
                current_weather = zone_weathers[-1]
            zone_weather[zone] = current_weather

        return zone_weather

    # Thanks to Rogueadyn's SaintCoinach library for this calculation
    def _calculate_weather_forecast_target(self, timestamp):
        bell = timestamp / 175
        increment = int(bell + 8 - (bell % 8)) % 24;

        totalDays = int(timestamp / 4200)
        calcBase = (totalDays * 0x64) + increment
        step1 = ((calcBase << 0xB) & 0x7fffffff) ^ calcBase
        step2 = (step1 >> 8) ^ step1

        return int(step2 % 0x64)
