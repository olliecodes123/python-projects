import json, requests, sys

#compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# download the Json data 

url = "http://api.openweathermap.org/data/2.5/forecast/city?id=%s&APPID=c6dd5202c06d13e80d1ecdc374fd3b85" % (location)
response = requests.get(url)
response.raise_for_status()

# load JSON data into a python variable
weatherData = json.loads(response.text)

#print weather description
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'],'-',w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'],'-',w[1]['weather'][0]['description'])
print()
print('Day after omorrow:')
print(w[2]['weather'][0]['main'],'-',w[2]['weather'][0]['description'])

