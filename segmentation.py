# Wai

# Twitter Distance
def tweet_distance(tw1, tw2):
	# Author: 	Joel Kemp
	# Precond: 	tw1, tw2 are strings
	# Returns: 	an integer count of similar words
	count = 0
	for word in tw1:
		if word in tw2:
			count += 1
	return count

# Kmeans