#We have a loud talking parrot. The "hour" input is the current hour time in the range 0..23. 
#We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble

def parrot(talk,hour):
    if (talk) and (hour <7 or hour >20):
        return True
    else:
        return False
print('talk = True, hour = 6 --> True: ' , parrot(True,6))
print('talk = True, hour = 7 --> False: ' , parrot(True,7))
print('talk = False, hour = 6 --> False: ' , parrot(False,6))
print('talk = True, hour = 21 --> True: ' , parrot(True,21))
print('talk = False, hour = 21 --> False: ' , parrot(False,21))
print('talk = False, hour = 20 --> False: ' , parrot(False,20))
print('talk = True, hour = 23 --> True: ' , parrot(True,23))
print('talk = False, hour = 23 --> False: ' , parrot(False,23))
print('talk = True, hour = 20 --> False: ' , parrot(True,20))
print('talk = False, hour = 12 --> False: ' , parrot(False,12))
