# Author: Joel Kemp
# Purpose: 	Used to prep a list of stop words into a usable format
file = open("stopwords2.txt")
data = []
for line in file:
	line = line.rstrip()
	if line == "\n" or line == "":
		continue
	data.append(line)
	
file.close()

file = open("stopwords3.txt", "w")
for d in data:
	file.write(d + "\n")
	
file.close()