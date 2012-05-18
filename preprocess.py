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
	Notes: 		Inplace modification of list
	"""
	while True:
		num_instances = data.count(s)
		finished = num_instances == 0
		if finished:
			break
		data.remove(s)

def removeStopWords(data):
	"""
	Purpose: 	Removes instances of stop words from the passed list, data
	Precond: 	Data is a list of strings
	Notes: 		Inplace modification of data
				Stop words loaded from a textfile in the data/ directory.
	"""
	try:	
		stop_words = load_stop_words()
		
		for sw in stop_words:
			if sw in data:
				# Remove all occurrences of that stop word
				removeAllOccurrences(sw, data)

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

def stem(data):
	"""
	Purpose: 	Computes the stem of each word in the passed word list
	Returns:	A list containing a stem for each word in the words list
	"""
	stems = []
	for w in data:
		s = stem(w)
		stems.append(s)		
	return stems

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
			print tokens
			
			# Remove stop words from the list of tokens
			removeStopWords(tokens)
			print "Stop word removal: ", tokens
			input()
			# Remove the stems
			tokens = stem(tokens)
			print "Stemmed: ", tokens
			input()
			
			# Convert the token list to a string representation
			token_string = "".join(tokens)

			# Store the processed tweets in a new file
			file_write.write(token_string + "\n")

		file_write.close()
	
	except Exception, e:
		print "Error:", e

main()