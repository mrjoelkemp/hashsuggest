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

		# Remove junk elements
		pieces = removeAllOccurrences(pieces, "")
		pieces = removeAllOccurrences(pieces, ":")
		pieces = removeAllOccurrences(pieces, "\"text\"")
		pieces = removeAllOccurrences(pieces, "\"\\\"")
		pieces = removeAllOccurrences(pieces, "}]")

		# Remove internal double quotes from tweets.
		# Tweets are enclosed with single quotes
		dub_quote = "\""
		for p in pieces:
			has_quotes = p.count(dub_quote) > 0		
			if has_quotes:
				p = p[1:-1]
			print p

		
		#print pieces

	except Exception, e:
		print "Exception: ", e

def removeAllOccurrences(data, s):
	"""
	Purpose: 	Removes all occurrences of s from the passed list, data.
	Precond: 	data = list
				s 	 = string
	Returns:	data with no instances of s
	"""
	while True:
		num_blanks = data.count(s)
		finished = num_blanks == 0
		if finished:
			break
		data.remove(s)
	return data		
main()