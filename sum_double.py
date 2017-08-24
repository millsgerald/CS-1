#Given two int values, return their sum. Unless the two values are the same, then return double their sum.
x = int(input('Enter value 1\n'))
y = int(input('Enter value 2\n'))
if x != y:
    print(x+y)
else:
    print((x+y)*2)
