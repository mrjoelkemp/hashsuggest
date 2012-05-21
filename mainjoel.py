# Author: 	Joel Kemp
# Purpose: 	Driver program
from preprocess import *
import segmentation
import random

def main():
	processed_tweets = "data/tweetsprocessedashton.txt"
	raw_tweets = "data/tweetsashton.txt"
	
	# Grab a stem -> word mapping from the file
	LUT = get_LUT(raw_tweets)

	# Open the tweet file
	file = open(processed_tweets)
	tweets = []
	for t in file:
		tweets.append(t.replace("\n", ""))

	print "Num tweets: ", len(tweets)

	# Training set
	subtweets = random.sample(tweets, len(tweets) // 3)
	print "Num training: ", len(subtweets)

	# Testing set
	testing = list(set(tweets) - set(subtweets))
	print "Num testing: ", len(testing)

	#clusters = segmentation.kmeans(subtweets, 5, 20, 0.8)


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