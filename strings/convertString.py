str = 'X-DSPAM-Confidence:0.8475'
index = str.find(':') + 1
print (index)
number = float(str[index:])
print (number)
print (type(number))
