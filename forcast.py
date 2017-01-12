from urllib2 import *
from parser import *
from ast import *

key = 'Insert Key Here'

#Finds the current condition for the weather based on location
def getKey(location, state):
	url = "http://dataservice.accuweather.com/locations/v1/search?q="+ location + "&apikey=" + key
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
	url = "http://dataservice.accuweather.com/currentconditions/v1/"+ location + "?apikey=" + key
	try:
		weather, length = parseList(urlopen(url).read())
		return "Weather Conditions: " + weather[0]['WeatherText'] + ", Temperature: " + weather[0]['Temperature']['Imperial']['Value'] + "F"
	except URLError, e:
		print "Error: ", e
		return None

def main():
	city = raw_input("What city do you want to know the weather of? ")
	state = raw_input("What state is this city in? ")
	print getWeather(getKey(city, state))

if __name__ == "__main__":main()
