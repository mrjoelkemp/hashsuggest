# Author: Joel Kemp
# Purpose: 	Used to prep a list of stop words into a usable format

# Join the two lists of stop words from two files
file = open("stopwords.txt")
data = []
# First file only contains comma separated list
words = []
for line in file:
	words = line.split(",")
file.close()

# Process the words and add to the list
for w in words:
	w = w.rstrip()
	w = w.lower()
	data.append(w)
print "Done with stopwords.txt"

# Open and process the second file
# Second file has words separated by newlines
file = open("stopwords2.txt")

for line in file:
	line = line.lower()
	line = line.rstrip()

	# Avoid adding duplicates
	if line in data:
		continue
	data.append(line)
file.close()
print "Done with stopwords2.txt"

# Store all the words to a text file separated by newlines.
file = open("stopwords3.txt", "w")

for d in data:
	file.write(d + "\n")
file.close()
print "Done creating stopwords3.txt"


"""
# OLD CODE
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
"""