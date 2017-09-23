# We have two monkeys, a and b. Accept the input telling if each is smiling. 
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

def smile(a,b):
    if(a and b) or not(a or b):
        return True
    else:
        return False
print('smile = True, True --> True:',smile(True,True))
print('smile = False, False --> True:',smile(False,False))
print('smile = True, False --> False:',smile(True,False))
print('smile = False, True --> False:',smile(False,True))
