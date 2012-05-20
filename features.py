# Author: 	Wai Khoo
# File: 	features.py
# Purpose: 	A collection of functions that aids clustering.

from sets import Set

# Twitter Distance
def tweet_distance(tw1s, tw2s):
	# Author: 	Joel Kemp
	# Modified by: Wai Khoo
	# Precond: 	tw1s, tw2s are strings
	# Returns: 	an integer count of similar words
	tw1 = tokenise(tw1s)
	tw2 = tokenise(tw2s)
	count = 0
	for word in tw1:
		if word in tw2:
			count += 1
	return count
	
# Compute term frequency from tweets and extract dominant term
def computeTF_DT(tweets):
	# Tokenise the string into words
	str_tweets = tokenise(joinString(tweets))
	
	# Remove duplicates
	unique_tweets = Set((word for word in str_tweets))

	# Compute frequency for each word and creating a dictionary
	tf = dict([(term, freq(term, str_tweets)) for term in unique_tweets])
	
	# Sort the term-frequency list in descending order and select the first item as dominant term
	result = sorted(tf.items(), key=lambda x:x[1], reverse=True)
	dt = result[0][0]
	
	return tf, dt
	
# Helper function to compute frequency
def freq(word, sentence):
	return sentence.count(word)
	
# break string up into tokens
def tokenise(string):
	""" break string up into tokens """
	string = string.replace("\s+", " ")
	string = string.lower()
	words = string.split(" ")
	return [word for word in words]

# Convert a list of tweets into a single string
def joinString(list):
	str_list = []
	for tweet in list:
		str_list.append(tweet + ' ')
	return ''.join(str_list)