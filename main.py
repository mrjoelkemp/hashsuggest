#! c:/Python27/python

# Author(s): 	Wai Khoo and Joel Kemp
# File: 		main.py
# Purpose: 		Entry point to our program

import cgi, cgitb
import sys
import segmentation 
import random

sys.stderr = sys.stdout

def main():
	# Obtain value from POST
	form = cgi.FieldStorage()
	k = int(form.getvalue('K')) # number of clusters
	cutoff = float(form.getvalue('Thres')) # Threshold
	iteration = int(form.getvalue('Iter')) # number of iteration
	queryTweet = form.getvalue('Tweet') # Query tweet
	
	# Open the tweet file
	file = open("data/tweetsprocessedashton.txt")
	tweets = []
	for t in file:
		tweets.append(t.replace("\n", ""))
		
	subtweets = random.sample(tweets, len(tweets)/2) # Use half of the dataset for training
	clusters = segmentation.kmeans(subtweets, k, iteration, (1.0 - cutoff)) # Since our notion of cutoff is reversed, we do (1.0 - cutoff)
	
	# Print some results out
	print '<br>'
	for i in range(len(clusters)):
		print "Cluster '%s': %s tweets<br>" % (clusters[i].dt, len(clusters[i].tweets))
		print "&nbsp;&nbsp;&nbsp;&nbsp;Centroid: %s<br><br>" % clusters[i].centroid

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Twitter Hashtag Suggestion Engine</title>'
print '</head>'
print '<body>'
main()
print '</body>'
print '</html>'