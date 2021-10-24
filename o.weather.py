from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from pyowm.utils import timestamps
import time

#Setting :
lang = 'EN'
city = 'City,EN'
key = 'api-key'

config_dict = get_default_config()
config_dict['language'] = lang
owm = OWM(key, config_dict)
mgr = owm.weather_manager()
obser = mgr.weather_at_place(city)
weather = obser.weather
status = weather.detailed_status
hum = weather.humidity
sunrise_date = weather.sunrise_time(timeformat='date')
sunrset_date = weather.sunset_time(timeformat='date')
wind_dict_in_meters_per_sec = obser.weather.wind()
wind_dict_in_meters_per_sec['speed']
temp_dict_kelvin = weather.temperature()
temp_dict_kelvin['temp_min']
temp_dict_kelvin['temp_max']
temp_dict_celsius = weather.temperature('celsius')
h = int(time.strftime("%H"))
h = h - 7
three_h_forecaster = mgr.forecast_at_place(city, '3h')
tomorrow = timestamps.tomorrow(h,0)
weath = three_h_forecaster.get_weather_at(tomorrow)
status2 = weath.detailed_status
temp_dict_kelvin2 = weath.temperature()
temp_dict_celsius2 = weath.temperature('celsius')
meteo = str(str(temp_dict_celsius['temp'])+"C "+str(status).replace('é','e').replace('è','e')+" "+str(temp_dict_celsius['feels_like'])+"C +"+str(temp_dict_celsius['temp_max'])+"C -"+str(temp_dict_celsius['temp_min'])+"C Hum:"+ str(hum)+"% Wind:"+str(wind_dict_in_meters_per_sec['speed']) +"m/s "+"Sun:"+str(sunrise_date.strftime('%H:%M:%S'))+" - "+str(sunrset_date.strftime('%H:%M:%S'))+" || Tomorrow at "+str(h)+"h : "+str(temp_dict_celsius2['temp'])+"C "+str(status2).replace('é','e').replace('è','e')+" "+str(temp_dict_celsius2['feels_like'])+"C")
print("Weather report : "+meteo)
