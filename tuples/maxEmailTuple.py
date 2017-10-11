# Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses from the line. 
# Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples 
# from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.
# Sample Line: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 Enter a file name: mbox-short.txt cwen@iupui.edu 5 
# Enter a file name: mbox.txt zqian@umich.edu 195

fhand = open("mbox.txt")
email_dict = dict()
for line in fhand:
    if line.startswith("From "):
        words = line.rstrip().split()
        sender = words[1]
        email_dict[sender] = email_dict.get(sender,0) + 1
        #for (k,v) in email_dict.items():
           # print(k,v)
        tups = email_dict.items()
        #print(tups)
tmp = list()
for k,v in email_dict.items():
    tmp.append((v,k))
#print(tmp)
tmp = sorted(tmp, reverse=True)
#print(tmp)
for v,k in tmp[:1]:
    print(k,v)
