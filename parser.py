#Parse list from string
def parseList(string):
	output = []
	count = 0
	strings = string.replace('"', "'").replace(' ', '')

	#Loops through the entire string
	while count < len(strings):
		#Skip over the list characters
		if strings[count] == "[" or strings[count] == "]":
			count += 1
			continue

		#Find the dictionary then append to list
		if strings[count] == "{":
			count += 1
			dictionary, length = parseDict(strings[count:])
			count += length
			output.append(dictionary)

	return output

#Parse dictionary from string
def parseDict(string):
	dictionary = []
	count = 0

	#Loops till it find the end of the dictionary
	while string[count] != "}":
		new_str = string[count:]

		#Key is the first character before ":"
		key = new_str.rsplit(':')[0]
		count += len(key) + 1
		new_str = string[count:]
		
		#Check value is '{' or just a regular value
		if new_str[0] == "{":
			count += 1
			value, length = parseDict(new_str[1:])
			count += length
			
		else:
			value = string[count:].rsplit(',')[0]
			if "}" in value:
				value = value.rsplit('}')[0]
				count += len(value)
			else:
				count += len(value) + 1
		dictionary.insert(0, (key.replace("'", ""), value))

	#Return the dictionary and the length of the string used
	return dict(dictionary), count + 1