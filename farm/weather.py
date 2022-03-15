import requests
from pprint import pprint

city = input('Enter your city : ')
url = 'https://api.openweathermap.org/data/2.5/weather?lat=77.5&lon=72.87&appid=4a94fa172697811530f4a06e0600ae13'.format(city)
res = requests.get(url)

data = res.json()

temp = data['main']['temp']
wind_speed = data['wind']['speed']

latitude = data['coord']['lat']
longitude = data['coord']['lon']

description = data['weather'][0]['description']

print('Temperature : {} degree celcius'.format(temp))
print('Wind Speed : {} m/s'.format(wind_speed))
print('Latitude : {}'.format(latitude))
print('Longitude : {}'.format(longitude))
print('Description : {}'.format(description))