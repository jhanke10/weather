def parseList(string):
	#Output and counter
	output = []
	count = 1

	#Fix the string if not fixed
	strings = string.replace('"', "'").replace(' ', '')

	#Items in the list
	item = ''

	#Loop until "]"
	while strings[count] != ']':
		#Check if dictionary within list
		if strings[count] == '{':
			dictionary, length = parseDict(strings[count:])
			count += length
			output.append(dictionary)
			continue

		#Check if list within list	
		if strings[count] == '[':
			lists, length = parseList(strings[count:])
			count += length
			output.append(lists)
			continue

		#Treat like normal list
		if strings[count] == ',':
			if item != '':
				output.append(item.replace("'", ""))
				item = ''
			count += 1
			continue

		#Keep adding to the item until it hits the end of list or comma
		item += strings[count]
		count += 1

	#For the last item if applicable
	if item != '':
		output.append(item.replace("'", ""))

	#Return the list and the length of the string used
	return output, count + 1

#Parse dictionary from string
def parseDict(string):
	#Output and counter
	dictionary = []
	count = 1

	#Fix the string if not fixed
	strings = string.replace('"', "'").replace(' ', '')

	#Value in the dictionary
	keys = False
	val = ''

	#Loops till "}"
	while strings[count] != '}':
		#Treat like normal dictionary
		if strings[count] == ',':
			if val != '' and keys:
				dictionary.insert(0, (key.replace("'", ""), val.replace("'", "")))
				val = ''
				keys = False
			count += 1	

		#Get the key for the item
		if not keys:
			key = strings[count:].rsplit(':')[0]
			count += len(key) + 1
			keys = True

		#Check if dictionary within dictionary
		if strings[count] == '{':
			value, length = parseDict(strings[count:])
			count += length
			dictionary.insert(0, (key.replace("'", ""), value))
			keys = False
			continue

		#Check if list within dictionary
		if strings[count] == '[':
			value, length = parseList(strings[count:])
			count += length
			dictionary.insert(0, (key.replace("'", ""), value))
			keys = False
			continue

		#Keep adding to the value
		val += strings[count]
		count += 1

	#For the last item if applicable
	if val != '' and keys:
		dictionary.insert(0, (key.replace("'", ""), val.replace("'", "")))

	#Return the dictionary and the length of the string used
	return dict(dictionary), count + 1
