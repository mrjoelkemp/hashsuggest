import segmentation 
import random

def main():
	# Open the tweet file
	file = open("data/tweetsprocessedashton.txt")
	tweets = []
	for t in file:
		tweets.append(t.replace("\n", ""))

	subtweets = random.sample(tweets, len(tweets)/2)
	clusters = segmentation.kmeans(subtweets, 20, 25, 0.5)

	for i in range(len(clusters)):
		print "len: %s, dt:%s" % (len(clusters[i].tweets), clusters[i].dt)

main()