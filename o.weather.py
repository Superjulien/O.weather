from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from datetime import datetime, timedelta
from pyowm.utils import timestamps
import argparse

# O.weather
# by superjulien 
# > https://github.com/Superjulien
# > https://framagit.org/Superjulien
# V1.09

# Configurations
LANG = 'EN'
CITY = 'City,EN'
API_KEY = 'api-key'
HOURS_TO_ADD = 7
HOURS_TO_ADD_TWO = 38
UNITS = 'celsius'  # Choose 'celsius' or 'fahrenheit'
VERS = 1.09

config_dict = get_default_config()
config_dict['language'] = LANG
owm = OWM(API_KEY, config_dict)
mgr = owm.weather_manager()

def get_weather_info(weather_obj):
    temperature = weather_obj.temperature(UNITS)
    temp_min = temperature['temp_min']
    temp_max = temperature['temp_max']
    feels_like = temperature['feels_like']
    current_temperature = temperature['temp']

    return {
        'detailed_status': weather_obj.detailed_status,
        'humidity': weather_obj.humidity,
        'wind_speed': weather_obj.wind().get('speed'),
        'temp_min': temp_min,
        'temp_max': temp_max,
        'feels_like': feels_like,
        'current_temperature': current_temperature,
        'sunrise': weather_obj.sunrise_time(timeformat='date'),
        'sunset': weather_obj.sunset_time(timeformat='date')
    }

def generate_ascii_table(now, weather_info, tomorrow_info, new_info, temp_unit_symbol, future_time, forecast_time_two):
    lines = [
        f"{now.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Temperature          | {weather_info['current_temperature']} {temp_unit_symbol}",
        f"Status               | {weather_info['detailed_status']}",
        f"Feels like           | {weather_info['feels_like']} {temp_unit_symbol}",
        f"Min/Max Temperature  | {weather_info['temp_min']}/{weather_info['temp_max']} {temp_unit_symbol}",
        f"Humidity             | {weather_info['humidity']}%",
        f"Wind Speed           | {weather_info['wind_speed']} m/s",
        f"Sunrise              | {weather_info['sunrise'].strftime('%H:%M:%S')}",
        f"Sunset               | {weather_info['sunset'].strftime('%H:%M:%S')}",
	F"{future_time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Temperature          | {tomorrow_info['current_temperature']} {temp_unit_symbol}",
        f"Status               | {tomorrow_info['detailed_status']}",
	f"{forecast_time_two.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Temperature          | {new_info['current_temperature']} {temp_unit_symbol}",
        f"Status               | {new_info['detailed_status']}",
    ]

    max_line_lengths = [len(line) for line in lines]
    max_line_length = max(max_line_lengths)
    formatted_lines = []
    header_line = '+' + '-' * (max_line_length + 4) + '+'
    for i, line in enumerate(lines):
        if i == 0 or i == 9 or i == 1 or i == 10 or i == 13 or i == 12:
            formatted_lines.append(header_line)
        formatted_lines.append(f"| {line.ljust(max_line_length + 2)} |")

    formatted_lines.append(header_line)
    ascii_table = '\n'.join(formatted_lines)
    print(f" Weather Report - {CITY}")
    return ascii_table

def main():
    observation = mgr.weather_at_place(CITY)
    current_weather = observation.weather
    weather_info = get_weather_info(current_weather)

    now = datetime.now()
    future_time = now + timedelta(hours=HOURS_TO_ADD)
    forecast_hour = future_time.hour

    tomorrow_forecaster = mgr.forecast_at_place(CITY, '3h')
    tomorrow_weather = tomorrow_forecaster.get_weather_at(timestamps.tomorrow(forecast_hour, 0))
    tomorrow_info = get_weather_info(tomorrow_weather)

    forecast_time_two = now + timedelta(hours=HOURS_TO_ADD_TWO)
    new_forecaster = mgr.forecast_at_place(CITY, '3h')
    new_weather = new_forecaster.get_weather_at(forecast_time_two)
    new_info = get_weather_info(new_weather)

    parser = argparse.ArgumentParser(description="Weather Information")
    parser.add_argument("-a", "--ascii", action="store_true", help="Generate an ASCII weather report")
    parser.add_argument("-v", "--version", action="store_true", help="Show the version number")
    args = parser.parse_args()

    temp_unit_symbol = '°C' if UNITS == 'celsius' else '°F'

    if args.version:
        print("O.weather version " + str(VERS))
        return    

    if args.ascii:
        ascii_table = generate_ascii_table(now, weather_info, tomorrow_info, new_info, temp_unit_symbol, future_time, forecast_time_two)
        print(ascii_table)
    else:
        print(f"Weather Report - {CITY}")
        print(f" > [{now.strftime('%Y-%m-%d %H:%M:%S')}] Temperature:{weather_info['current_temperature']}{temp_unit_symbol}")
        print(f"   - Status:{weather_info['detailed_status']} [Min:{weather_info['temp_min']}{temp_unit_symbol}/Max:{weather_info['temp_max']}{temp_unit_symbol}]")
        print(f"   - Feels like:{weather_info['feels_like']}{temp_unit_symbol}")
        print(f"   - Humidity:{weather_info['humidity']}% Wind:{weather_info['wind_speed']}m/s")
        print(f"   - Sunrise:{weather_info['sunrise'].strftime('%H:%M:%S')} Sunset:{weather_info['sunset'].strftime('%H:%M:%S')}")
        print(f" > [{future_time.strftime('%Y-%m-%d %H:%M:%S')}] Temperature:{tomorrow_info['feels_like']}{temp_unit_symbol}")
        print(f"   - Status:{tomorrow_info['detailed_status']}")
        print(f" > [{forecast_time_two.strftime('%Y-%m-%d %H:%M:%S')}] Temperature:{new_info['feels_like']}{temp_unit_symbol}")
        print(f"   - Status:{new_info['detailed_status']}")

if __name__ == "__main__":
    main()
