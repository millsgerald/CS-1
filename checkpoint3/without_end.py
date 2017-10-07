# Given a string, return a version without the first and last char, so "Hello" yields "ell". 
# The string length will be at least 2.

def withoutend(a):
    x = (len(a))
    #print(x)  # to check the lenght of x
    y = (x-1)
    #print(y)  to check the lenght of y
    return (a[1:y])
print('without_end: ' , withoutend('Hello'))
print('without_end: ' , withoutend('java'))
print('without_end: ' , withoutend('coding'))
print('without_end: ' , withoutend('code'))
print('without_end: ' , withoutend('ab'))
print('without_end: ' , withoutend('Chocolate!'))
print('without_end: ' , withoutend('kitten'))
print('without_end: ' , withoutend('woohoo'))
