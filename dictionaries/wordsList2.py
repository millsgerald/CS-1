# Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesn't matter what the values are. Then you can use the in operator as a fast way to check whether a 
# string is in the dictionary



fhand = open('words.txt')
wordslist = dict()
for words in fhand:
    words = words.rstrip()
    words = words.split()
    for word in words:
        wordslist[word] = wordslist.get(word,0) + 1
    print(wordslist)

print ("reptitive" in wordslist)  # Should return TRUE if the word is found in the dictionary
