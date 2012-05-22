# Author: 	Joel Kemp
# File: 	suggestion.py
# Purpose: 	A module of functions to facilitate hashtag suggestion

from features import *
from preprocess import *
import segmentation
import random
import cluster

def suggest_hashtag(tweet, clusters, lut_source = "data/tweetsashton.txt"):
	"""
	Purpose: 	Entry point to the suggestion engine. 
	Precond:	tweet = a raw tweet string from the user.
				K = number of clusters.
	Notes: 		Since the user can change the number of clusters, we need it to be adjustable.
	Returns: 	The top hashtag suggestion.
	TODO: 		Change to suggest the top M hashtag_stem
	"""

	query_tokens = process_query(tweet)
	# String representation of the processed tweet
	processed_tweet = get_tweet_string(query_tokens)

	closest = get_query_cluster(processed_tweet, clusters)
	# Hashtag is the dominant term of the closest cluster
	hashtag_stem = closest.dt

	# Get the original word (w/ stem)
	# Grab a stem -> word mapping from the file
	LUT = get_LUT(lut_source)
	hashtag = LUT[hashtag_stem]

	return hashtag

def load_tweets(filename):
	"""
	Purpose: 	Loads tweet strings from file and does minor processing
	Returns: 	A list of strings where each element is a line from the file.
	"""
	# Open the tweet file
	file = open(filename)
	tweets = []
	
	# Grab all of the tweets
	for t in file:
		t = t.lower()
		tweet = t.replace("\n", "")
		# Avoid duplicates
		if tweet in tweets:
			continue
		
		tweets.append(tweet)

	return tweets

def get_query_cluster(processed_tweet, clusters):
	"""
	Purpose: 	Finds the cluster of tweets that are closest to the passed tweet
	Precond: 	processed_tweet = string without stop words and stems
				clusters = a list of Cluster objects
	Returns: 	A Cluster object that best fits the processed tweet
	"""

	closest_cluster = None
	smallest_distance = None

	for i in range(len(clusters)):

		# Grab the centroid tweet
		centroid_tweet = clusters[i].centroid

		# Compute the tweet distance
		distance = tweet_distance(centroid_tweet, processed_tweet)
		
		# If it's out first comparison
		if smallest_distance == None or distance < smallest_distance:
			smallest_distance = distance
			closest_cluster = clusters[i]

	return closest_cluster