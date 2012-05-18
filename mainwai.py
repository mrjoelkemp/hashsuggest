import cluster
from features import tweet_distance

def main():
	data = ["This is is is tweet1", "Another tweet2 again again and again", "yet so another tweet3, tweet3 again", "omg, so many tweets4"]
	
	c = cluster.Cluster(data[0])
	c.update(data)
	print c

	data.append("tweet tweet, tweet5")
	c.update(data)
	print c
	
main()