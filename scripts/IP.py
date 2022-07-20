import json, requests
from urllib.request import urlopen

class IP:

	def __init__(self):

		IP = requests.get('http://ip.42.pl/raw').text  # Get the IP

		# Get the location information of IP
		url = 'https://ipapi.co/{}/json/'.format(IP)
		response = urlopen(url)
		data = json.load(response)

		# Extract individual information from IP
		self.IP = data['ip']
		self.org = data['org']
		self.city = data['city']
		self.country = data['country']
		self.latitude = data['latitude']
		self.longitude = data['longitude']
		self.region = data['region']


if __name__ == "__main__":
	ip = IP()
	print(ip.IP);