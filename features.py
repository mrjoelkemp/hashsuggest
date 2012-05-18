# File Author: Wai Khoo

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
	str_tweets = tokenise(joinString(tweets))
	unique_tweets = Set((word for word in str_tweets))
	
	tf = dict([(term, freq(term, str_tweets)) for term in unique_tweets])
	
	result = sorted(tf.items(), key=lambda x:x[1], reverse=True)
	dt = result[0][0]
	
	return tf, dt
	
# Helper function to compute frequency
def freq(word, sentence):
	return sentence.count(word)
	
# break string up into tokens
def tokenise(string):
	""" break string up into tokens """
	string = string.replace(".", "")
	string = string.replace(",", "")
	string = string.replace("\s+", " ")
	string = string.lower()
	words = string.split(" ")
	return [word for word in words]

# Convert a list into a single string
def joinString(list):
	str_list = []
	for tweet in list:
		str_list.append(tweet + ' ')
	return ''.join(str_list)