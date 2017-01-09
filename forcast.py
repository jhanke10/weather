from urllib2 import *
from parser import *
from ast import *

key = "aVGsC0oQ5qdiS58gmAqrFhM4cbozeIMc"

#Finds the current condition for the weather based on location
def getKey(location, state):
	url = "http://dataservice.accuweather.com/locations/v1/search?q="+ location + "&apikey=" + key
	try:
		cities = urlopen(url).read()
		print cities
		# for city in cities:
			# if city['AdministrativeArea']['ID'] == state:
				# return city['Key']
	except URLError, e:
		print "Error: ", e
		return None

#Gets the weather in Fahrenheit and the condition
def getWeather(location):
	url = "http://dataservice.accuweather.com/currentconditions/v1/"+ location + "?apikey=" + key
	try:
		weather = urlopen(url).read()
		return weather[0]['WeatherText'] + " " + weather[0]['Imperial']['Value'] + "F"
	except URLError, e:
		print "Error: ", e
		return None

def main():
	# city = raw_input("What city do you want to know the weather of? ")
	# state = raw_input("What state is this city in? ")
	lists = parseList("[{'something' : 1, 'else' : {'hi' : 2,'bye' : 3}, 'hi': 4}, {'lol': 4}]")
	print type(lists)
	print lists

if __name__ == "__main__":main()