# Author: 	Joel Kemp
# Purpose: 	This file contains the code necessary to convert the 
#			pulled JSON twitter feeds into usable text files with one tweet per line
# Notes: 	THis code is sloppy because it's pretty much throw-away

import simplejson
import re
import string

def main():
	
	try:

		# Open the json text file
		file = open("data/joel.json")

		# The json file is encoded as a single string
		for line in file:
			data = line

		# Regex elements
		re1='.*?'	# Non-greedy match on filler
		re2='("text")'	# Double Quote String 1
		re3='(.)'	# Any Single Character 1
		re4='(".*?")'	# Double Quote String 2

		rg = re.compile(re1+re2+re3+re4,re.IGNORECASE|re.DOTALL)
		
		# Split the long string based on the created regex
		# This results in a list with the tweets, some text used to identify the tweet regions,
		#	and a few empty strings.
		pieces = rg.split(data)

		# Remove junk elements from the list
		removeJunk(pieces)

		# Remove internal double quotes from each tweet.
		removeDoubleQuotes(pieces)

		# Remove embedded links from each tweet
		links = ["http", "www"]
		for link in links:
			removeFromElements(link, pieces)

		# Remove @ handles
		handle = "@"
		removeFromElements(handle, pieces)

		# Remove all punctuation
		punctuation = list(string.punctuation)
		punctuation.append("")
		for punc in punctuation:
			removeFromElements(punc, pieces, True)

		removeAllOccurrences("\\", pieces)
		removeAllOccurrences("", pieces)

		# Write the tweets to file
		file = open("data/tweets.txt", "w")
		for p in pieces:
			file.write(p + "\n")
		print "Done writing tweets to file."
		
	except Exception, e:
		print "Exception: ", e

def removeJunk(data):
	# Remove junk elements from every tweet
	junk = ["", ":", "\"text\"", "\"\\\"", "}]"]
	for j in junk:
		removeAllOccurrences(j, data)

def removeFromElements(substring, data, exact=False):
	"""
	Purpose: 	Strips the substring from the elements of data, if it exists
	Precond: 	exact = whether or not we should remove the words or just the chars of the subtring.
	Notes:		Inplace modification of the list
	"""
	for i in range(len(data)):
		elem = data[i]
		contains = elem.count(substring)
		if contains:
			if exact:
				removed = removeExactSubstring(substring, elem)
			else:
				removed = removeFromString(substring, elem)
			data[i] = removed

def removeFromString(substring, s):
	"""
	Purpose: 	Removes the word in the passed string, s, containing the passed substring
	Notes: 		This is more general than removeExactSubstring() since 
				we're removing the entire word, not just the matching chars
	Returns: 	A new string with the contents of s minus the substring-contained words
	"""
	result = ""
	words = s.split()
	for word in words:
		contains = word.count(substring) > 0
		# Build a string of non-occurrences.
		if not contains:
			result += word + " "
	# Trim off the excess whitespace
	result = string.rstrip(result)
	return result

def removeExactSubstring(substring, s):
	"""
	Purpose: 	Removes the substring from the string, s by replacing the substring by a space
	Returns: 	The modified string
	""" 
	result = string.replace(s, substring, "")
	return result

def removeDoubleQuotes(data):
	"""
	Purpose: 	Tweets are enclosed with single quotes
	Notes: 		Inplace modification of list
	"""
	dub_quote = "\""
	for i in range(len(data)):
		p = data[i]
		has_quotes = p.count(dub_quote) > 0		
		if has_quotes:
			data[i] = p[1:-1]
		
def removeAllOccurrences(s, data):
	"""
	Purpose: 	Removes all occurrences of s from the passed list, data.
	Precond: 	data = list
				s 	 = string
	Notes: 		Inplace modification of list
	"""
	while True:
		num_instances = data.count(s)
		finished = num_instances == 0
		if finished:
			break
		data.remove(s)

main()