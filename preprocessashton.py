# Author: 	Joel Kemp
# Purpose: 	Script to preprocess tweets and store them in a file for later consumption.

from preprocess import *
def main():
	try:
		# Open the tweet file
		file = open("tweetsashton.txt")
		
		# Grab all of the tweets from file.
		tweets = []
		for tweet in file:
			tweet = tweet.lower()
			# split the tweet into tokens
			tokens = tweet.split()
			tweets.append(tokens)

		file.close()

		file_write = open("tweetsprocessedashtonbig.txt", "w")
		
		for tokens in tweets:
			# Remove stop words from the list of tokens
			stopped = removeStopWords(tokens)
			
			# Remove all words smaller than the threshold
			big_words = removeSmallWords(stopped, 4)

			# Remove the stems
			stems = removeStems(big_words)
			
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