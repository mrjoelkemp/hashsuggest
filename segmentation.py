# Author: 	Wai Khoo
# File: 	segmentation.py
# Purpose: 	Perform kmean on twitter feed

import random
import cluster
from features import tweet_distance
from features import tokenise

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
			# Compute distances to each of the cluster
			dist = [float(tweet_distance(t, clusters[i].centroid))/min(len(tokenise(t)), len(tokenise(clusters[i].centroid))) for i in range(len(clusters))]
			
			# Find the max, which indicate the most similarity
			maxDist = max(dist)
			idx = dist.index(maxDist)
		
			# If the tweet doesn't fit into any cluster (below a threshold), randomly assign it to a cluster, otherwise, assign it to the cluster with maximum distance
			if maxDist < cutoff:
				lists[random.sample(range(k), 1)[0]].append(t)
			else:
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