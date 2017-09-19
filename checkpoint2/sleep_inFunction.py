# Write a program to accept Weekday and Vacation values. 
# Weekday is True if it is a weekday, and the vacation is True if we are on vacation. 
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

def sleepin (weekday, vacation):
    if(not weekday or vacation):
        return True
    else:
        return False
print ('sleepin = False, False:',sleepin(False,False)) #sleepin(False,False) = True
print ('sleepin = True, False:',sleepin(True,False)) #sleepin(True,False) = False
print ('sleepin = False, True:',sleepin(False,True)) #sleepin(False,True) = True
