Write a python program simulating driver's license provision. 
#Accept the age of the driver and his total number of practice hours. 
#If driver’s age is below 16, do not issue license. 
#if 16 or above then check if number of practice hours is more than(ie. >) 200. if > 200, issue license otherwise don’t.

def license():
    age = 0
    hours = 0
    while True:
        try:
            age = int(input('Enter your age\n'))
            hours = int(input('Enter the number of practice hours\n'))   
            if age < 16:
                print ('You are to young to have a license')
            elif hours < 200:
                print('You have not done enough practise hours')
            else:
                print('Congratulations here is your license')
            break
        except: 
            print('Enter a valid entry')
license()
