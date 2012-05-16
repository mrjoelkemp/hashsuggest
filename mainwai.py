import cluster

def main():
	data = ["This is tweet1", "Another tweet 2", "yet another tweet 3", "omg, so many tweets 4"]
	
	c = cluster.Cluster(data)
	
	print c
	
main()