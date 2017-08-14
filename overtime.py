#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hours = input('How many hours have you worked this week?\n')
rate = input('What is your hourly rate?\n')
npay = float(hours) * float(rate)
#ohours calculates any overtime for hours in excess of 40 hours if any
ohours = (float(hours) - 40) * (float(rate) * 1.5)
#opayn calualtes the normal 40 hour week
opayn = 40 * float(rate)
if float(hours) < 40:
    print ('Your Gross Pay for this week is ${0:.2f} '.format(npay))
elif float(ohours) > 0:   
    print ('Your Gross Pay including overtime for this week is ${0:.2f} '.format(opayn+ohours))
