#Write a program to accept Weekday and Vacation values. 
#Weekday is True if it is a weekday, and the vacation is True if we are on vacation. 
#We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
w = input('Is it a weekday y/n?\n').lower() # w = weekday
v = input('Is it a vacation day? y/n?\n').lower() # v = vacation
if w == 'n' and v == 'n':
    print('True')
elif w == 'y' and v == 'n':
    print('False')
elif w == 'n' and v == 'y':
    print('True')
elif w == 'y' and v == 'y':
    print('True')

