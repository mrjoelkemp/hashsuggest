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
	hashtags = [hashtag for tweet, hashtag in tweets_hashtags]
	# Get the set of hashtags
	hashtag_set = set(hashtags)
	# Compute the frequency of the hashtags about the output.
	counts = [hashtags.count(hashtag) for hashtag in hashtag_set]
	hashtag_freqs = zip(list(hashtag_set), counts)

	print "<h3> Testing Set Hashtag Frequencies </h3>"
	print "<table style='width: 200px;'>"
	print "<tr><td><b>Hashtag</b></td><td><b>Frequency</b></td></tr>"
	for hashtag, freq in hashtag_freqs:
		print "<tr>"
		print "<td>", "#" + hashtag, "</td>"
		print "<td>", freq, "</td>"
		print "</tr>"
	print "</table>"

def print_average_number_words(tweets_hashtags):
	num_tweets = len(tweets_hashtags)
	sum_nums = 0

	for tweet, hashtag in tweets_hashtags:
		tweet_words = tweet.split()
		sum_nums += len(tweet_words)

	average_number_words = sum_nums / num_tweets
	print "<h3> <b>Average tweet length: </b>", average_number_words, "words.</h3>"

def print_cluster_centroids(clusters):
	print "<h3> Cluster Centroids: </h3>"
	for i in range(len(clusters)):
		print "Cluster #" + str(i) + ":", clusters[i].centroid, "<br/>"
