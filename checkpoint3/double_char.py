# Given a string, return a string where for every char in the original, there are two chars.

def double(a):
    for letter in a:
        index = 0
        new_str = ''
        while index < len(a):
            double_str = a[index]*2
            new_str = new_str + double_str
            index = index + 1
        return(new_str)        
print('double_char: ' , double('The'))
print('double_char: ' , double('AAbb'))
print('double_char: ' , double('Hi-There'))
print('double_char: ' , double('Word'))
print('double_char: ' , double('!!'))
print('double_char: ' , double('"'))
print('double_char: ' , double('a'))
print('double_char: ' , double('.'))
print('double_char: ' , double('aa'))

## The following works but output is not 100% as I would expect
#def double(a):
#    for letter in a:
#        print (letter, letter, end = ' ')
#double('The\n')
#double('AAbb\n')
#double('Hi-There\n')
#double('Word\n')
#double('!!\n')
#double("''\n")
#double('a\n')
#double('.\n')
#double('aa\n')
