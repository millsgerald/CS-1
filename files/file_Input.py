fname = input ('Enter the file name:\n')
fhand = open(fname)
counter = 0
total = 0
for line in fhand:
   if line.startswith('X-DSPAM-Confidence:'):
       counter = counter + 1
       number = float(line[21:])
       total = number + total
average = total/counter    
print('Average SPAM confidence', average)
