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
	
	# Grab all of the tweets
	for t in file:
		t = t.lower()
		tweet = t.replace("\n", "")
		# Avoid duplicates
		if tweet in tweets:
			continue
		
		tweets.append(tweet)

	print "Num tweets: ", len(tweets)

	# Training set
	num_training = len(tweets) // 3
	subtweets = random.sample(tweets, num_training)
	
	# Testing set
	testing = [tweet for tweet in tweets if tweet not in subtweets]
	
	# Perform k-means on the subtweets
	clusters = segmentation.kmeans(subtweets, 5, 20, 0.8)

	#########
	## DEBUG: Sample querying
	#########
	query = "I want to save the world by rescuing Uganda and all of its children with my ex-wife Demi."
	
	query_tokens = process_query(tweet)
	# String representation of the processed tweet
	query_string = get_tweet_string(query_tokens)



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