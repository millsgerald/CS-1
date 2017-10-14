# The program below reads a dataset containing reviews of Donna Tartt’s The Goldfinch in the Amazon book review. 
# These reviews have been stored in a simple tab separated file, which is nothing more than a plain text file with columns. 
# The table contains four columns: review score, url, review title and review text.
# Your task is to put comments on each line explaining what it does. First few lines are already commented for you

#Import required library
import urllib.request

#Load the data from remote location (URL)
file = urllib.request.urlopen("https://gist.githubusercontent.com/twielfaert/a0972bf366d9aaf6cb1206c16bf93731/raw/dde46ad1fa41f442971726f34ad03aaac85f5414/Donna-Tartt-The-Goldfinch.csv")

# Create a variable called "f" and store the data from the URL as read only.
f = file.read()

#Transform the bitstream into strings
text = f.decode(encoding='utf-8',errors='ignore')

# Split the text using the "new line" as the seperator. This would split for each line.
lines = text.split("\n")

# Creates a blank dictionary called "counts"
counts = dict()
# creates a counter with a starting value of 0
counter = 0
#for loop. Loops the proceeding line through each line in the file.
for line in lines:
    #loops through each line in the file stripping the white space and splitting the file based on the seperator \t (tab)
  l = line.strip().split("\t")
  
  #creates 4 seperate lists for each column in the file. The square brackets indicate the postion of the split text to 
  #be stored in each list.
  score = l[0] 
  id = l[1]
  title = l[2]
  review = l[3]
  
  #Add the score "text" to the counts dictionary as the key and adds a counter of how many times score occurs as a value.
  counts[score] = counts.get(score, 0) + 1
  # adds 1 to the value of counter then loops back to the for loop above. Continues looping until all lines have been read.
  counter = counter + 1 

  # after all lines have been read print the counter total
print(str(counter))
#prints the length of the string 'lines'
print(str(len(lines)))

# creates a Tuple with stores the score (key) and score counter (value) as paired values.
for key, val in counts.items():
    #print the total value for each score stored in the Tuple.
    print (key, val)
