#Write a python program simulating driver's license provision. 
#Accept the age of the driver and his total number of practice hours. 
#If driver’s age is below 16, do not issue license. 
#if 16 or above then check if number of practice hours is more than(ie. >) 200. if > 200, issue license otherwise don’t.

def license(age,hours):
    if(age>15) and (hours>199):
        return True
    else:
        return False
print ('license = True, True:',license(True,True)) #license(True,True) = True
print ('license = False, False:',license(True,True)) #license(True,True) = False   not sure if this us valid
