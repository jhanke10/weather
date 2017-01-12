from urllib2 import *
from parser import *
from ast import *

key = 'Insert Key Here'

#Finds the current condition for the weather based on location
def getKey(location, state):
	url = "http://dataservice.accuweather.com/locations/v1/search?q="+ location.replace(" ", "") + "&apikey=" + key
	try:
		cities, length = parseList(urlopen(url).read())
		for city in cities:
			if city['AdministrativeArea']['ID'].lower() == state.lower():
				return city['Key']
	except URLError, e:
		print "Error: ", e
		return None

#Gets the weather in Fahrenheit and the condition
def getWeather(location):
	if location == None:
		print 'Cannot find city/state'
		return None
	url = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/"+ location + "?apikey=" + key
	try:
		weather, length = parseList(urlopen(url).read())
		print weather
		for forecasts in weather:
			date = forecasts['DateTime'].rsplit('T')[0]
			time = forecasts['DateTime'].rsplit('T')[1].rsplit('-')[0]
			if int(time.rsplit(':')[0]) > 12:
				time = str(int(time.rsplit(':')[0]) - 12) + 'PM'
			else:
				if int(time.rsplit(':')[0]) == 12:
					time = str(12) + 'PM'
				elif int(time.rsplit(':')[0]) == 0:
					time = str(12) + 'AM'
				else:
					time = time.rsplit(':')[0] + 'AM'
			print "Date/Time: " + date + ", " + time + " Temperature: " + forecasts['Temperature']['Value'] + "F\nChance of Rain: " + forecasts['PrecipitationProbability'] + "% Weather Conditions: " + forecasts['IconPhrase'] + "\nDaytime: " + forecasts['IsDaylight'] + "\n"
		return 'Found Forecasts for this city/state'
	except URLError, e:
		print "Error: ", e
		return None

def main():
	city = raw_input("What city do you want to know the weather of? ")
	state = raw_input("What state is this city in? ")
	print getWeather(getKey(city, state))

if __name__ == "__main__":main()