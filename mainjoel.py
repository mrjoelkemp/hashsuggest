# Author: 	Joel Kemp
# Purpose: 	Driver program
from preprocess import *


def main():
	processed_tweets = "data/tweetsprocessedashton.txt"

	raw_tweets = "data/tweetsashton.txt"
	
	# Grab a stem -> word mapping from the file
	LUT = get_LUT(raw_tweets)

	for stem, word in LUT.items():
		print stem, "->", word


	# uniques = get_unique_words(raw_tweets)
	# for unique in uniques:
	# 	print unique


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

rem()