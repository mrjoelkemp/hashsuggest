import segmentation 
import random

def main():
#	data = ["This is is is tweet1", "Another tweet2 again again and again", "yet so another tweet3, tweet3 again", "omg, so many tweets4", "tweet tweet, tweet5"]

#	clusters = segmentation.kmeans(data, 4, 0.8)
#	print clusters
#	print clusters[3].dt
#	print clusters[3].tf

	# Open the tweet file
	file = open("data/tweetsprocessedashton.txt")
	tweets = []
	for t in file:
		tweets.append(t.replace("\n", ""))

	subtweets = random.sample(tweets, len(tweets)/3)
	clusters = segmentation.kmeans(subtweets, 5, 20, 0.8)

	for i in range(len(clusters)):
		print "len: %s, dt:%s" % (len(clusters[i].tweets), clusters[i].dt)
	
	print clusters[4]
main()