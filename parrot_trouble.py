#We have a loud talking parrot. The "hour" input is the current hour time in the range 0..23. 
#We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble
hour = (input('Enter the current hour? 0 thru 23.\n'))
if (float(hour) >= 7) and (float(hour) <= 20):
    print('False')
else:
    print('True')
