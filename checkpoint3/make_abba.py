# Given two strings, a and b, return the result of putting them together in the order abba, 
# e.g. "Hi" and "Bye" returns "HiByeByeHi".

def abba(a,b):
    return a + b + b + a
print('abba:' , abba('Hi','Bye'))
print('abba:' , abba('Yo','Alice'))
print('abba:' , abba('What','Up'))
print('abba:' , abba('aaa','bbb'))
print('abba:' , abba('x','y'))
print('abba:' , abba('x',''))
print('abba:' , abba('','y'))
print('abba:' , abba('Bo','Ya'))
print('abba:' , abba('Ya','Ya'))
