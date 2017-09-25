#You are driving a little too fast, and a police officer stops you. 
#Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
#If speed is 60 or less, the result is 0. 
#If speed is between 61 and 80 inclusive, the result is 1. 
#If speed is 81 or more, the result is 2. 
#Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

def ticket(speed,bday):
        if speed in range(1,61) and (not bday):
            return 0
        elif speed in range(61,81) and (not bday):
            return 1
        elif (speed > 80) and (not bday):
            return 2
        elif speed in range(1,66)and (bday):
            return 0
        elif speed in range(66,86) and (bday):
                return 1
        elif (speed > 85) and (bday):
                return 2
print ('speed = 60, bday = False --> 0: ',ticket(60,False))
print ('speed = 65, bday = False --> 1: ',ticket(65,False))
print ('speed = 65, bday = True --> 0: ',ticket(65,True))
print ('speed = 80, bday = False --> 1: ',ticket(80,False))
print ('speed = 85, bday = False --> 2: ',ticket(85,False))
print ('speed = 85, bday = True --> 1: ',ticket(85,True))
print ('speed = 70, bday = False --> 1: ',ticket(70,False))
print ('speed = 75, bday = False --> 1: ',ticket(75,False))
print ('speed = 75, bday = True --> 1: ',ticket(75,True))
print ('speed = 40, bday = False --> 0: ',ticket(40,False))
print ('speed = 40, bday = True --> 0: ',ticket(40,True))
print ('speed = 90, bday = False --> 2: ',ticket(90,False))
