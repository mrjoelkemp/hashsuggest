# Author: 	Wai Khoo
# File: 	segmentation.py
# Purpose: 	Perform kmean on twitter feed

import random
import cluster
from features import tweet_distance

# Kmeans
# tweets is a list of tweets
# k is the number of clusters
# maxRound is the maximum number of iteration
# cutoff is a convergence threshold
def kmeans(tweets, k, maxRound, cutoff):
	init = random.sample(tweets, k) # randomly sample k tweets
	clusters = [cluster.Cluster(t) for t in init] # Use the init set as k separate clusters
	
	round = 0
	while round < maxRound:
		print 'Round #%s<br>' % round
		lists = [ [] for c in clusters] # Create an empty list for each cluster
		for t in tweets:
			# Get the distance for t to the centroid of 1st cluster
			big_dist = tweet_distance(t, clusters[0].centroid)
			idx = 0
			for i in range(len(clusters[1:])): # For all the other cluster
				dist = tweet_distance(t, clusters[i+1].centroid)
				
				# Assign t to the appropriate cluster (i.e. with the most similarity)
				if dist > big_dist:
					big_dist = dist
					idx = i + 1
			
			# Append t to the closest cluster
			lists[idx].append(t)

		# Update the clusters
		biggest_shift = 0.0
		for i in range(len(clusters)):
			shift = clusters[i].update(lists[i])
			biggest_shift = max(biggest_shift, shift)
			
		# If the clusters aren't shifting much (i.e. twitter distance remain high), break and return the results
		if biggest_shift > cutoff:
			break
		
		round = round + 1
		
	print "Done clustering...<br>"
	return clusters