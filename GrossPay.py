#Write a program to prompt the user for hours and rate per hour to compute gross pay
hours = input('How many hours have you worked this week?\n')
rate = input('What is your hourly rate?\n')
pay = float(hours) * float(rate)
print ('Your Gross Pay for this week is ${0:.2f} '.format(pay))
