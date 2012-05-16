# Author: Wai Khoo

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