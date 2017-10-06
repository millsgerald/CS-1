# Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop 
# (see Section [maximumloop]) to find who has the most messages and print how many messages the person has.
# Enter a file name: mbox-short.txt cwen@iupui.edu 5 Enter a file name: mbox.txt zqian@umich.edu 195



fhand = open("mbox.txt")
email_dict = dict()
for line in fhand:
    if line.startswith("From "):
        words = line.rstrip().split()
        sender = words[1]
        email_dict[sender] = email_dict.get(sender,0) + 1
#print (email_dict)
emailcount = 0
emailaddress = 0
for email,count in email_dict.items():
    if emailcount is None or count > emailcount:
        emailcount = count
        emailaddress = sender
print(emailaddress, emailcount)
