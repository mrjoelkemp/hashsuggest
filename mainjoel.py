# Author: 	Joel Kemp
# Purpose: 	Driver program
from preprocess import *

def main():
	try:
		# Open the tweet file
		file = open("data/tweetsashton.txt")
		
		# Grab all of the tweets from file.
		tweets = []
		for tweet in file:
			tweet = tweet.lower()
			# split the tweet into tokens
			tokens = tweet.split()
			tweets.append(tokens)

		file.close()

		file_write = open("data/tweetsprocessedashton.txt", "w")
		
		for tokens in tweets:
			# Remove stop words from the list of tokens
			stopped = removeStopWords(tokens)
			
			# Remove the stems
			stems = removeStems(stopped)
			
			# Get a string representation of the list
			tweet_string = get_tweet_string(stems)
			
			# Prevent blanks from being stored
			if tweet_string == "":
				continue 
			
			# Store the processed tweets in a new file
			file_write.write(tweet_string + "\n")

		file_write.close()
		print "Done creating preprocessed tweet file."

	except Exception, e:
		print "Error:", e

main()