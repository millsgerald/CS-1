#Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def value(a,b):
    if (a != b):
        return a + b
    else:
        return (a+b)*2
print('a = 1 , b = 2 --> 3: ', value(1,2))
print('a = 3 , b = 2 --> 5: ', value(3,2))
print('a = 2 , b = 2 --> 8: ', value(2,2))
print('a = -1 , b = 0 --> -1: ', value(-1,0))
print('a = 3 , b = 3 --> 12: ', value(3,3))
print('a = 0 , b = 0 --> 0: ', value(0,0))
print('a = 0 , b = 1 --> 1: ', value(0,1))
print('a = 3 , b = 4 --> 7: ', value(3,4))
