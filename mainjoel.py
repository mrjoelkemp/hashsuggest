# Author: 	Joel Kemp
# Purpose: 	Driver program
from suggestion import *

def main():
	
	#########
	## DEBUG: Sample querying
	#########
	source = "data/tweetsprocessedashton.txt"
	tweets = load_tweets(source)
	
	# Training set is 2/3 the number of tweets
	num_training = (2 * len(tweets)) // 3
	# System training and testing tweets
	training = random.sample(tweets, num_training)
	testing = [tweet for tweet in tweets if tweet not in training]
	
	# Perform k-means on the training set
	K = 10
	clusters = segmentation.kmeans(training, K, 20, 0.8)
	for i in range(len(clusters)):
		print "len: %s, dt:%s" % (len(clusters[i].tweets), clusters[i].dt)

	for tweet in testing:
		hashtag = suggest_hashtag(tweet, clusters)
		print "Query Tweet: ", query
		print "Suggested hashtag: #" + hashtag


def rem():
	# Remove all of the small words from tweetashton.txt
	raw_tweets = "data/tweetsashton.txt"

	file = open(raw_tweets)
	output = open("data/tweetsashtonbig.txt", "w")

	for tweet in file:
		words = tweet.split()
		words = removeSmallWords(words)
		tweet_string = get_tweet_string(words)

		# Write to the second file.
		output.write(tweet_string + "\n")

	file.close()
	output.close()

main()