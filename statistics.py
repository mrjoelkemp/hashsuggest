# Author: 	Joel Kemp
# File: 	statistics.py
# Purpose: 	Helper functions for printing statistics about the system's output.

def print_hashtag_frequency(tweets_hashtags):
	"""
	Purpose: 	Prints the frequency table for hashtags based on the passed
				list of tuples.
	Precond: 	tweets_hashtags is a tuple consisting of a tweet
				and its suggested hashtag.
	"""
	hashtags = [hash for tweet, hash in tweets_hashtags]
	# Get the set of hashtags
	hashtag_set = set(hashtags)
	# Compute the frequency of the hashtags about the output.
	counts = [hashtags.count(hash) for hash in hashtag_set]
	hashtag_freqs = zip(list(hashtag_set)), counts)
	print "TODO"