#Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, 
#return a string of the form "7:00" indicating when the alarm clock should ring. 
#Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". 
#Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
day = input('''Enter the day of the week in the following format
0 = Sun
1 = Mon
2 = Tue
3 = Wed
4 = Thu
5 = Fri
6 = Sat
\n''')
vac = input('Are you on vacation?y/n\n').lower()

if vac == 'n' and (int(day) == 0):
    print('10:00')
elif vac == 'n' and (int(day) == 6):
    print('10:00')
elif vac == 'n' and (int(day) >=1) and (int(day)<=5):
    print('07:00')
else:
    if vac == 'y' and (int(day) == 0):
        print('off')
    elif vac == 'y' and (int(day) == 6): 
        print('off')
    elif vac == 'y' and (int(day) >=1) and (int(day)<=5):
        print('10:00')