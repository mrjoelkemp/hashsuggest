import cluster

def main():
	data = ["This is is is tweet1", "Another tweet2 again again and again", "yet so another tweet3, tweet3 again", "omg, so many tweets4"]
	
	c = cluster.Cluster(data)
	c.computeTF_DT()
#	print c
	
main()