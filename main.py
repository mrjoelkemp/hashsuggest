#! c:/Python27/python

# Author(s): 	Wai Khoo and Joel Kemp
# File: 		main.py
# Purpose: 		Entry point to our program

import cgi, cgitb
import sys
from suggestion import *
import random
import segmentation

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
	# System training and testing tweets
	training = random.sample(tweets, num_training)
	testing = [tweet for tweet in tweets if tweet not in training]
	
	# Perform k-means on the training set
	clusters = segmentation.kmeans(training, k, iteration, (1.0 - cutoff))
	for i in range(len(clusters)):
		print "len: %s, dt:%s" % (len(clusters[i].tweets), clusters[i].dt)

	# Grab a stem -> word mapping from the file
	lut_source = "data/tweetsashton.txt"
	LUT = get_LUT(lut_source)

	#for tweet in testing:
	#	hashtag = suggest_hashtag(tweet, clusters, LUT)
	#	print tweet, "#" + hashtag
	hashtag = suggest_hashtag(queryTweet, clusters, LUT)
	print "<h2> Suggested Hashtag Output: </h2>"
	print queryTweet, "<b>#" + hashtag + "</b>"

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Twitter Hashtag Suggestion Engine</title>'
print '</head>'
print '<body>'
main()
print '</body>'
print '</html>'