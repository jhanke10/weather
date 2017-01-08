from urllib2 import *
from ast import *

key = "aVGsC0oQ5qdiS58gmAqrFhM4cbozeIMc"

#Finds the current condition for the weather based on location
def getKey(location, state):
	url = "http://dataservice.accuweather.com/locations/v1/search?q="+ location + "&apikey=" + key
	try:
		cities = urlopen(url).read().replace('"', "'")
		print cities
		# for city in cities:
			# return 0
			# if city["AdministrativeArea"]["ID"] == state:
				# return city["Key"]
	except URLError, e:
		print "Error: ", e
		return None

#Parse list from string
def parseList(string):
	output = []
	count = 0

	while count < range(len(string)):
		if string[count] == "[" or string[count] == "]":
			continue
		if string[count] == "{":
			dictionary = parseDict(string[count:])
			count += len(dictionary)
		count += 1

#Parse dictionary from string
def parseDict(string):
	dictionary = {}
	count = 0
	while string[count] != "}":
		key = string.rpartition(':')[0]
		count += len(key)
		if string[len(key):][0] == "{":
			value = parseDict(string[len(key):][1])
		else:
			value = string[len(key):].rpartition(',')[0]




#Gets the weather in Fahrenheit and the condition
def getWeather(location):
	url = "http://dataservice.accuweather.com/currentconditions/v1/"+ location + "?apikey=" + key
	try:
		weather = urlopen(url).read()
		return weather[0]["WeatherText"] + " " + weather[0]["Imperial"]["Value"] + "F"
	except URLError, e:
		print "Error: ", e
		return None

def main():
	city = raw_input("What city do you want to know the weather of? ")
	state = raw_input("What state is this city in? ")
	print getKey(city, state)

if __name__ == "__main__":main()