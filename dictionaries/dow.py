# Write a program that categorizes each mail message by which day of the week the commit was done. 
# To do this look for lines that start with "From", then look for the third word and keep a running count of each of the 
# days of the week. At the end of the program print out the contents of your dictionary (order does not matter).
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Sample Execution:
# python dow.py Enter a file name: mbox-short.txt {'Fri': 20, 'Thu': 6, 'Sat': 1}

fhand = open("mbox-short.txt")
dow_dict = dict()
for line in fhand:
    if line.startswith("From "):
        words = line.rstrip().split()
        dayofweek = words[2]
        dow_dict[dayofweek] = dow_dict.get(dayofweek,0) + 1
print (dow_dict)


# the following code does not produce the correct result. I am not sure why the day[2] does not work?
#fhand = open('mbox-short.txt')
#dow_dict = dict()
#for line in fhand:
#    if line.startswith('From '):
#        day = line.rstrip().split()
#        for dow in day:
#            dow_dict[day[2]] = dow_dict.get(day[2],0) + 1  # day[2] extracts only the 3rd word from the line
#print(dow_dict)
