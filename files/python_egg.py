fname = input ('Enter the file name:\n')
try:
    fhand = open(fname)
except:
        if fname == ('na na boo boo'):
            print("NA NA BOO BOO TO YOU - You have been punk'd!")
            quit()
        else:
            print('File cannot be opened', fname)
            quit()
counter = 0
for line in fhand:
    #line = line.rstrip()
    if line.startswith('Subject'):
        counter = counter + 1
print('There were ', counter, 'subject lines in mbox.txt')
