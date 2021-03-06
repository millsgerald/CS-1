## Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program
#hours = input('How many hours have you worked this week?\n')
#try:
#    ival1 = int(hours)
#except:
#    ival1 = -1
#if ival1 > 0:
#    rate = input('What is your hourly rate?\n')
#    try:
#        ival2 = int(rate)
#    except:
#        ival2 = -1
#    if ival2 > 0:
#        pay = float(hours) * float(rate)
#        print ('Your Gross Pay for this week is ${0:.2f} '.format(pay))
#    else:
#        print('Please enter numeric input')
#else:
#    print('Please enter numeric input')

# The following is a simplified version of the above provided by Engramar.
# The drawback of this is it handles the except for both inputs together while the above code handles them seperatly.
#import sys
try:
    hours = int(input('How many hours have you worked this week?\n'))
    rate = input('What is your hourly rate?\n')
except:
    print ('Please enter a numeric value')
pay = float(hours) * float(rate)
print('Your Gross pay for this week is ${0:.2f}'.format (pay))
#sys.exit()
