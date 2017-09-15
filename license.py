# Write a python program simulating driver's license provision. Accept the age of the driver and his total number of practice
#  hours. If drivers age is below 16, do not issue license. if 16 or above then check if number of practice hours is 
#  more than(ie. >) 200. if > 200, issue license otherwise don't.

age = int(input('Enter your age\n'))
hours = int(input('Enter the number of practice hours\n'))
if age < 16:
	print ('you are to young to have a license')
elif hours < 200:
	print(' you have not done enough practise hours')
else:
	print('Congratulations here is your license')
