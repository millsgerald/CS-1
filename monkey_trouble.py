#We have two monkeys, a and b. Accept the input telling if each is smiling. 
#We are in trouble if they are both smiling or if neither of them is smiling. 
#Return True if we are in trouble.
a = input('Is monkey 1 smiling? y/n?\n').lower() # a = monkey1
b = input('Is monkey 2 smiling? y/n?\n').lower() # b = monkey2
if a == 'n' and b == 'n':
    print('True')
elif a == 'y' and b == 'n':
    print('False')
elif a == 'n' and b == 'y':
    print('false')
elif a == 'y' and b == 'y':
    print('True')
