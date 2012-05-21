# Author: 	Joel Kemp
# File: 	preprocess.py
# Purpose: 	A collection of functions that strip unnecessary characters from tweets.
# Notes:	Tweet preprocessing is done offline, so this doesn't have to be a module.
from stemming.porter2 import stem	# Stemming algorithm


def preprocess(data):
	"""
	Purpose: 	Main helper to facilitate the removal of stop words and stems from the passed data.
	Precond: 	data = list of strings
	Returns: 	A list of preprocessed strings
	"""
	processed = list(data)

	processed = removeStopWords(processed)
	processed = removeStems(processed)

	return processed

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
	for d in data:
		stemList.append(stem(d))
	return stemList

def get_LUT(filename):
	""" 
	Purpose: 	Generates a lookup table with stem -> tweet_word mappings 
				for each word in the file identified by the passed filname.
	
	Precond: 	filename = string filename of the file to be loaded and parsed.
	
	Returns: 	A dictionary of stem -> tweet_word mappings
	
	Usage: 		If you have a stem and want to retrieve an idea of the original tweet text, 
				stems_words = get_LUT("tweets.txt")
				stems_words["includ"] will yield "include"
	
	Notes: 		If the stem already exists, we want the smallest
				word that generates that stem. 
				If we don't do this, then we'll only get the last
				word that generated the stem.
				The smallest word is closer to the root of the word;
				this should be more helpful.
	"""
	stems_words = {}

	# Generate the unique list of words from the file
	unique_words = get_unique_words(filename)

	# Get the stems of each word
	stems = removeStems(unique_words)
	
	# Join the lists into tuples
	stems_uniques = zip(stems, unique_words)

	for stem, word in stems_uniques:
		exists = stem in stems_words

		smallest_word = word
		if exists:
			current_word = stems_words[stem]
			current_is_smaller = len(current_word) < len(word)
			if current_is_smaller:
				smallest_word = current_word

		stems_words[stem] = smallest_word 

	return stems_words

def get_unique_words(filename):
	"""
	Purpose: 	Generates a list of unique (non-repeating) words from the 
				file identified by the passed filename.
	Precond: 	filename = string filename of the file containing the words to be loaded
	Returns: 	A list of unique strings.
	"""
	words = []
	try:
		file = open(filename)
		for tweet in file:
			word_list = tweet.split()
			
			# Remove the stop words
			stopped = removeStopWords(word_list)

			for word in stopped:
				# If the word is already in the list, then move on
				if word in words:
					continue
				
				# Otherwise, add the unique word to the list of words
				words.append(word)

		file.close()

	except Exception, e:
		raise e

	return words

def get_tweet_string(data):
	"""
	Precond: 	data = a list of strings
	Returns: 	A single string including the passed items 
				from the passed list, data.
	Format: 	Each datum is whitespace separated.
	"""

	# Convert the token list to a string representation
	token_string = ""
	
	for s in data:
		token_string += s + " "
	
	token_string = token_string.rstrip()
	
	return token_string