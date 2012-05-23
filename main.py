#! c:/Python27/python

# Author(s): 	Wai Khoo and Joel Kemp
# File: 		main.py
# Purpose: 		Entry point to our program

import cgi, cgitb
import sys
from suggestion import *
import random
import segmentation
from statistics import *

sys.stderr = sys.stdout

def main():
	# Obtain value from POST
	form = cgi.FieldStorage()
	k = int(form.getvalue('K')) # number of clusters
	cutoff = float(form.getvalue('Thres')) # Threshold
	iteration = int(form.getvalue('Iter')) # number of iteration
	queryTweet = form.getvalue('Tweet') # Query tweet
	
	source = "data/tweetsprocessedashton.txt"
	tweets = load_tweets(source)
	
	# Training set is 2/3 the number of tweets
	num_training = (2 * len(tweets)) // 3
	training = random.sample(tweets, num_training)
	testing = [tweet for tweet in tweets if tweet not in training]
	
	# Perform k-means on the training set
	clusters = segmentation.kmeans(training, k, iteration, (1.0 - cutoff))

	# Grab a stem -> word mapping from the file
	lut_source = "data/tweetsashton.txt"
	LUT = get_LUT(lut_source)

	# Get the raw, unprocessed tweets
	raw_tweets = load_tweets(lut_source)

	#Print raw tweets for testing set instead of the processed testing
	raw_testing = []
	
	# for each raw tweet:
	for raw in raw_tweets:
		proc = process_query(raw)
		proc_string = get_tweet_string(proc)

		# If the string is in the training, then continue
		if proc_string not in training:
			# Otherwise, store the *raw* string in the raw_testing
			raw_testing.append(raw)

	hashtags = [suggest_hashtag(raw, clusters, LUT) for raw in raw_testing]
	testing_tweets_hashtags = zip(raw_tweets, hashtags)

	# Compute statistics
	print "<h2> Statistics </h2>"
	print_hashtag_frequency(testing_tweets_hashtags)
	


	# Query Tweet Suggestion
	hashtag = suggest_hashtag(queryTweet, clusters, LUT)
	print "<h2> Suggested Hashtag Output: </h2>"
	print queryTweet, "<b style='font-size: 18px'>#" + hashtag + "</b>"
	print "<p>Suggested hashtag: #" + hashtag + "<p>"

	# Testing Set Suggestions
	print "<h2> Testing Set Output: </h2>"
	print "<table style='width: 750px;'>"
	print "<tr><td><b>Tweet</b></td><td><b>Suggested Hashtag</b></td></tr>"
	for raw, hashtag in testing_tweets_hashtags:
		print "<tr>"
		print "<td>", raw, "</td>"
		print "<td>", "#" + hashtag, "</td>"
		print "</tr>"
	print "</table>"

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Twitter Hashtag Suggestion Engine</title>'
print '</head>'
print '<body>'
main()
print '</body>'
print '</html>'