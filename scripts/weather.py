import requests
import json
from .IP import IP

# Icon dictionary for relative images
icon_lookup = {
	'clear-day': "assets/Sun.png",  # clear sky day
	'wind': "assets/Wind.png",   #wind
	'cloudy': "assets/Cloud.png",  # cloudy day
	'partly-cloudy-day': "assets/PartlySunny.png",  # partly cloudy day
	'rain': "assets/Rain.png",  # rain day
	'snow': "assets/Snow.png",  # snow day
	'snow-thin': "assets/Snow.png",  # sleet day
	'fog': "assets/Haze.png",  # fog day
	'clear-night': "assets/Moon.png",  # clear sky night
	'partly-cloudy-night': "assets/PartlyMoon.png",  # scattered clouds night
	'thunderstorm': "assets/Storm.png",  # thunderstorm
	'tornado': "assests/Tornado.png",    # tornado
	'hail': "assests/Hail.png"  # hail
}

def get_weather():
	'''
	Get formatted json of weather data for current day
	'''
	ip = IP()  # Get current location information

	# Get json from dark skys api
	APIKEY = '6b4e2599041ea02b9f19e4e86ae23f59'
	LAT, LON = ip.latitude, ip.longitude
	URL = 'https://api.darksky.net/forecast/{}/{},{}'.format(APIKEY, LAT, LON)
	r = requests.get(URL)
	json = r.json()

	temperatureHigh = json['daily']['data'][0]['temperatureHigh']
	temperatureLow = json['daily']['data'][0]['temperatureLow']
	week_summary = json['daily']['summary']
	# Get current and hourly data
	currently = json['currently']
	hourly = json['hourly']
	#print(hourly['data'])
	# Fetch important information for display
	title = currently['summary']
	icon = icon_lookup[currently['icon']]
	temperature = int((int(round(currently['temperature']))-32)*5/9)
	desc = hourly['summary'].rstrip('.')

	return {'title':title, 'icon':icon, 'temperature':temperature, 'desc':desc, 'temperatureHigh':temperatureHigh, 'temperatureLow':temperatureLow, 'week_summary':week_summary}


def get_weather_script():
	'''
	Return formatted news update for the day
	'''
	data = get_weather()
	script = """It is currently {0} at {1} degrees fahrenheit today with a high of {2} degrees fahrenheit and a low of {3} 
	degrees fahrenheit. Today it will be {4} and there will be {5}""".format(data['title'], data['temperature'], data['temperatureHigh'], data['temperatureLow'], data['desc'], data['week_summary'])
	return ' '.join(script.lower().split())  # Format and remove whitespace from string


if __name__ == "__main__":
	print(get_weather_script())
