#Write a python program simulating driver's license provision. 
#Accept the age of the driver and his total number of practice hours. 
#If driver’s age is below 16, do not issue license. 
#if 16 or above then check if number of practice hours is more than(ie. >) 200. if > 200, issue license otherwise don’t.

def license(age,hours):
    if(age>15) and (hours>199):
        return True
    else:
        return False
print ('license = Age 20, Hours 340 True:',license(20,340)) #license(20,340) = True
print ('license = age 15, Hours 340 False:',license(15,340)) #license(15,340) = False
print ('license = age 20, Hours 150 False:',license(20,150)) #license(20,150) = False
print ('license = age 15, Hours 199 False:',license(15,150)) #license(15,150) = False
print ('license = age 16, Hours 200 True:',license(16,200)) #license(15,150) = True
