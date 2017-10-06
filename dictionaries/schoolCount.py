# This program records the domain name (instead of the address) where the message was sent from instead of 
# who the mail came from (i.e., the whole email address). 
# At the end of the program, print out the contents of your dictionary.
# python schoolcount.py Enter a file name: mbox-short.txt {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7, 
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

fhand = open("mbox-short.txt")
school_dict = dict()
for line in fhand:
    if line.startswith("From "):
        words = line.rstrip().split()
        email = words[1] # extract the second word which includes email and school
        emailsplit = email.split('@')  #Double Split Program
        school = emailsplit[1]   # extracts the second word which is the school, leaves the enmail address
        school_dict[school] = school_dict.get(school,0) + 1
print (school_dict)
