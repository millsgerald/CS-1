#When squirrels get together for a party, they like to have cigars. 
#A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
#Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
#Return True if the party with the given values is successful, or False otherwise.

def party(weekend,cigars):
    if ((weekend) and (cigars > 39)) or (not weekend) and (cigars> 39 and cigars < 61): 
        return True
    else:
        return False
print('weekend = False, cigars = 30 --> False: ' , party(False,30))
print('weekend = False, cigars = 50 --> True: ' , party(False,50))
print('weekend = True, cigars = 70 --> True: ' , party(True,70))
print('weekend = True, cigars = 30 --> False: ' , party(True,30))
print('weekend = True, cigars = 50 --> True: ' , party(True,50))
print('weekend = False, cigars = 60 --> True: ' , party(False,60))
print('weekend = False, cigars = 61 --> False: ' , party(False,61))
print('weekend = False, cigars = 40 --> True: ' , party(False,40))
print('weekend = False, cigars = 39 --> False: ' , party(False,39))
print('weekend = True, cigars = 40 --> True: ' , party(True,40))
print('weekend = True, cigars = 39 --> False: ' , party(True,39))
