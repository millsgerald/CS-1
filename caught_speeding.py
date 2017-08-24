#You are driving a little too fast, and a police officer stops you. 
#Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
#If speed is 60 or less, the result is 0. 
#If speed is between 61 and 80 inclusive, the result is 1. 
#If speed is 81 or more, the result is 2. 
#Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

speed = input('Enter your speed\n')
bday = input('Is it your Birthday today?y/n\n').lower()
if bday == 'n' and (int(speed) <=60):
    print('0')
elif bday == 'n' and (int(speed) >=61) and (int(speed)<=80):
    print('1')
elif bday == 'n' and (int(speed) >=81):
    print('2')
else:
    if bday == 'y' and (int(speed) <=65):
        print('0')
    elif bday == 'y' and (int(speed) >=66) and (int(speed)<=86):
        print('1')
    elif bday == 'y' and (int(speed) >=87):
        print('2')