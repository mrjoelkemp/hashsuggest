# Author: 	Joel Kemp
# Purpose: 	This file contains the code necessary to convert the 
#			pulled JSON twitter feeds into usable text files with one tweet per line

import simplejson
import re

def main():
	# Open the json text file
	file = open("data/joel.json")

	# The json file is encoded as a single string
	for line in file:
		data = line

	try:
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
			removeElementsContaining(link, pieces)

		# Remove @ handles
		handle = "@"
		removeElementsContaining(handle, pieces)

		#for p in pieces:
		#	print p

	except Exception, e:
		print "Exception: ", e

def removeJunk(data):
	# Remove junk elements from every tweet
	junk = ["", ":", "\"text\"", "\"\\\"", "}]"]
	for j in junk:
		removeAllOccurrences(j, data)

def removeElementsContaining(s, data):
	"""
	Purpose: 	Removes elements from data containing s
	Notes: 		Inplace modification of list
	""" 
	for p in data:
		contains = p.count(s) > 0
		if contains:
			print p
			data.remove(p)


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