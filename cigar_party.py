#When squirrels get together for a party, they like to have cigars. 
#A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
#Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
#Return True if the party with the given values is successful, or False otherwise.
try:
    cigar = input('How many cigars are at the party?\n') 
    weekend = input('Is it the weekend? y/n\n').lower()

    if (int(cigar) >= 40) and weekend == 'y':
        print('True')
    elif (int(cigar) >=40) and (int(cigar) <=60) and weekend == 'n':
        print('True')
#else:
#    if weekend != 'n':
#        print('not a valid entry for weekend') 
#    elif weekend != 'y':
#        print('not a valid entry for weekend')    
    else:
        print('False')   
except:
    print("Enter a number for the 'number of cigars'")