# Author: 	Wai Khoo
# File: 	cluster.py
# Purpose: 	Definition of class Cluster

from features import tweet_distance
from features import computeTF_DT
from features import tokenise

class Cluster:
	# Init the object
	def __init__(self, data):
		if len(data) == 0: 
			raise Exception("ILLEGAL: empty cluster")
		
		self.tweets = [data]	# store a list of tweets
		self.centroid = data	# identify one of the tweets as centroid; initially it's just one tweet
		self.tf, self.dt = computeTF_DT(self.tweets)	# term frequency, dominant term		
		
	# Printing out the data
	def __repr__(self):
		print "Cluster '%s': %s tweets" % (self.dt, len(self.tweets))
		for t in self.tweets:
			if t == self.centroid:
				print "***\t%s" % t
			else:	
				print "\t%s" % t
		return ''
	
	# Update the cluster with new membership and return the deviation of centroid (normalized)
	def update(self, data):
		# Save the old centroid and recompute TF_DT
		old_centroid = self.centroid
		self.tweets = data
		self.tf, self.dt = computeTF_DT(self.tweets)
		self.centroid = self.calculateCentroid()
		return float(tweet_distance(old_centroid, self.centroid)) / min(len(tokenise(old_centroid)), len(tokenise(self.centroid)))
		
	# Calculate centroid of the tweets set, that is picking one of the tweets as centroid
	def calculateCentroid(self):
		# If there's no tweets in the cluster, return
		if len(self.tweets) == 0:
			return ''
	
		# Generate a list of twitter_distance
		t_dist = []
		for t in self.tweets:
			t_dist.append(tweet_distance(t, self.centroid))
		
		# Computing average distance of all the tweet_distance
		avgDist = round(float(sum(t_dist))/len(self.tweets))
		
		# Find the minimum difference in distance and returning that tweet
		closest_dist = [abs(x-avgDist) for x in t_dist]
		min_index, min_val = min(enumerate(closest_dist), key=lambda x:x[1])

		return self.tweets[min_index]
		
	def computeMaxNormalizedDist(self, tweet):
		maxDist = 0
		idx = 0
		
		for i, t in enumerate(self.tweets):
			dist = tweet_distance(t, tweet)
			
			if dist > maxDist:
				maxDist = dist
				idx = i
				
		return float(maxDist) / min(len(tokenise(tweet)), len(tokenise(self.tweets[idx])))
		
	def computeMaxNormalizedDist2(self, tweet, cutoff):
		cnt = 0
		
		for t in self.tweets:
			normDist = float(tweet_distance(t, tweet)) / min(len(tokenise(t)), len(tokenise(tweet)))
			if normDist >= cutoff:
				cnt = cnt + 1
				
		return cnt