# This program counts the distribution of the hour of the day for each of the messages. 
# You can pull the hour from the "From" line by finding the time string and then splitting that string into parts 
# using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, 
# sorted by hour as shown below.
# Sample Execution:
# python timeofday.py Enter a file name: mbox-short.txt 04 3 06 1 07 1 09 2 10 3 11 6 14 1 15 2 16 4 17 2 18 1 19 1

fhand = open("mbox-short.txt")
time_dict = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.rstrip().split()
        hour = words[5]
        hoursplit = hour.split(':')
        #print(hoursplit)
        single_hour = hoursplit[0]
        #print(single_hour)
        time_dict[single_hour] = time_dict.get(single_hour,0) + 1
        tups = time_dict.items()
tmp = list()
for k,v in time_dict.items():
    tmp.append((k,v))
tmp = sorted(tmp)
for v,k in tmp[:]:
    print(v,k, end = ' ')
