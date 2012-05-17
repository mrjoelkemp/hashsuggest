# Author: Wai Khoo

from sets import Set

class Cluster:
	# Init the object
	def __init__(self, data):
		self.tweets = data	# store a list of tweets
		self.centroid = ''	# identify one of the tweets as centroid
		self.tf = []		# term frequency
		self.dt = ''		# dominant term
		
	# Printing out the data
	def __repr__(self):
		print 'Cluster %s: %s' % (self.dt, len(self.tweets))
		for t in self.tweets:
			print t
			
		return ''
		
	# Retrieval functions for data members
	def getTweets(self):
		return self.tweets
		
	def getCentroid(self):
		return self.centroid
		
	def getTF(self):
		return self.tf
		
	def getDT(self):
		return self.dt
		
	# Set centroid (c is a string)
	def setCentroid(self, c):
		self.centroid = c
		
	# Compute term frequency from tweets and extract dominant term
	def computeTF_DT(self):
		str_tweets = self.tokenise(self.joinString(self.tweets))
		unique_tweets = Set((word for word in str_tweets))
		
		self.tf = dict([(term, self.freq(term, str_tweets)) for term in unique_tweets])
		
		result = sorted(self.tf.items(), key=lambda x:x[1], reverse=True)
		self.dt = result[0][0]
		
	# Helper function to compute frequency
	def freq(self, word, sentence):
		return sentence.count(word)
		
	# break string up into tokens
	def tokenise(self, string):
		""" break string up into tokens """
		string = string.replace(".", "")
		string = string.replace(",", "")
		string = string.replace("\s+", " ")
		string = string.lower()
		words = string.split(" ")
		return [word for word in words]
	
	# Convert a list into a single string
	def joinString(self, list):
		str_list = []
		for tweet in list:
			str_list.append(tweet + ' ')
		return ''.join(str_list)