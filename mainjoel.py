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



main()