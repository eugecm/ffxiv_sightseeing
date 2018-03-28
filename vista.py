import json


def load_vistas(filename):
    vistas = []
    with open(filename, 'r') as f:
        vista_data = json.load(f)
        for vista in vista_data['vistas']:
            vistas.append(Vista(**vista))
    return vistas


class Vista:

    def __init__(self, entry=0, name="", location="", map_location="", weather="", time="", emote=""):
        self.entry = entry
        self.name = name
        self.location = location
        self.map_location = map_location
        self.weather = weather
        self.time = time
        self.emote = emote

    @staticmethod
    def _to_time_int(time_str):
        if time_str.endswith('AM'):
            if time_str == '12AM':
                return 0
            return int(time_str[:-2])
        elif time_str.endswith('PM'):
            if time_str == '12PM':
                return 12
            return int(time_str[:-2]) + 12
        else:
            return int(time_str)

    def is_available(self, weather, eorzea_epoch):
        if not weather.upper() in self.weather.upper().split('/'):
            return False

        hour_now = int((eorzea_epoch / 3600) % 24)

        raw_start, raw_end = self.time.split('-')
        hour_start = self._to_time_int(raw_start)

        # If the start time does not end in AM/PM, use the suffix from end_time
        if not raw_start.endswith('M'):
            hour_start = self._to_time_int(raw_start + raw_end[:-2])

        # End time will always have a suffix so we can trust this is accurate
        hour_end = self._to_time_int(raw_end)

        if hour_end < hour_start:
            return (hour_now > hour_start) or (hour_now < hour_end)
        else:
            return hour_start <= hour_now < hour_end

    def __repr__(self):
        return '<Vista: entry={entry} name="{name}" weather="{weather}" time="{time}" location="{location}">'.format(**self.__dict__)
