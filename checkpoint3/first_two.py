# Given a string, return the string made of its first two chars, so the String "Hello" yields "He". 
# If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty 
# string "" yields the empty string "".
 
def firsttwo(a):
    return (a[:2])
print('first_two: ' , firsttwo('Hello'))
print('first_two: ' , firsttwo('abcdefg'))
print('first_two: ' , firsttwo('ab'))
print('first_two: ' , firsttwo('a'))
print('first_two: ' , firsttwo(''))
print('first_two: ' , firsttwo('Kitten'))
print('first_two: ' , firsttwo('hi'))
print('first_two: ' , firsttwo('hiya'))
