# Write a program that reads a file and prints the letters in decreasing order of frequency. 
# Your program should convert all the input to lower case and only count the letters a-z. 
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. 
# Find text samples from several different languages and see how letter frequency varies between languages. 
# Compare your results with the tables at wikipedia.org/wiki/Letter_frequencies.

import string
fname = input('Enter file name mbox-short.txt or mbox.txt: ')
try:
	fhandle = open(fname)
except:
	print ('File cannot be opened:'), fname
	exit()
letters = dict()
for line in fhandle:
    remove_digits = str.maketrans(line,line, string.digits)
    line = line.translate(remove_digits)
    remove_punct = str.maketrans(line,line, string.punctuation)
    line = line.translate(remove_punct)
    line = line.lower()
    line = line.split()
    for t in line:
        word = list(t)
        for letter in word:
            letters[letter] = letters.get(letter,0) + 1
letterlist = []
for letter, count in letters.items():
	letterlist.append( (count, letter) )
letterlist.sort(reverse=True)
for count, letter in letterlist:
	print (letter, count)
