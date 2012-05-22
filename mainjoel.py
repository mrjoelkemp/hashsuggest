# Author: 	Joel Kemp
# Purpose: 	Driver program
from suggestion import *

def main():
	
	#########
	## DEBUG: Sample querying
	#########
	query = "I want to save the world by rescuing Uganda and all of its children with my ex-wife Demi."
	
	num_clusters = 15
	hashtag = suggest_hashtag(query, num_clusters)

	print hashtag


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