# Author: 	Joel Kemp
# File: 	preprocess.py
# Purpose: 	A collection of functions that strip unnecessary characters from tweets.
# Notes:	Tweet preprocessing is done offline, so this doesn't have to be a module.
from stemming.porter2 import stem	# Stemming algorithm

def removeAllOccurrences(s, data):
	"""
	Purpose: 	Removes all occurrences of s from the passed list, data.
	Precond: 	data = list
				s 	 = string
	Returns: 	A copy of the list with the instances of s removed.
	"""
	copy = list(data)
	while True:
		num_instances = copy.count(s)
		finished = num_instances == 0
		if finished:
			break
		copy.remove(s)
	return copy

def removeStopWords(data):
	"""
	Purpose: 	Removes instances of stop words from the passed list, data
	Precond: 	Data is a list of strings
	Returns: 	A copy of data with the stop words removed
	Notes: 		Stop words loaded from a textfile in the data/ directory.
	"""
	try:	
		copy = list(data)
		stop_words = load_stop_words()
		
		for sw in stop_words:
			if sw in copy:
				# Remove all occurrences of that stop word
				copy = removeAllOccurrences(sw, copy)
		return copy

	except Exception, e:
		print "removeStopWords:", e

def load_stop_words():
	"""
	Purpose:	Loads the stop words from file.
	Notes: 		The file is currently hardcoded.
	Returns:	A list of lowercase strings where each string is a stop word.
	"""
	file = open("data/stopwords.txt")
	stop_words = []
	for line in file:
		line = line.rstrip()
		stop_words.append(line)
	file.close()
	return stop_words

def removeStems(data):
	"""
	Purpose: 	Computes the stem of each word in the passed word list
	Returns:	A list containing a stem for each word in the words list
	"""
	stemList = []
	print "removeStems: Data=", data
	for d in data:
		stemList.append(stem(d))
	return stemList

def main():
	try:
		# Open the tweet file
		file = open("data/tweetsashton.txt")
		
		# Grab all of the tweets from file.
		tweets = []
		for tweet in file:
			tweet = tweet.lower()
			# split the tweet into tokens
			tokens = tweet.split()
			tweets.append(tokens)

		file.close()

		file_write = open("data/tweetsprocessedashton.txt", "w")
		for tokens in tweets:
			# Remove stop words from the list of tokens
			stopped = removeStopWords(tokens)
			
			# Remove the stems
			stems = removeStems(stopped)
			print "Stemmed: ", stems
			
			# Convert the token list to a string representation
			token_string = ""
			for s in stems:
				token_string += s + " "
			token_string = token_string.rstrip()
			
			print "TokenString: ", token_string
			input()
			# Store the processed tweets in a new file
			file_write.write(token_string + "\n")

		file_write.close()
	
	except Exception, e:
		print "Error:", e

main()