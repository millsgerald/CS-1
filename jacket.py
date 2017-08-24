#Write a program to accept the temperature value and to tell a person to bring heavy jacket if temperature is < 20, 
#if temperature is between 20 and 30, bring light jacket. if temperature > 30, do not bring any jacket
temp = int(input('Enter current temperature\n'))
if (int(temp) < 20):
    print ('Bring a heavy jacket')
elif (int(temp) >=20 and (int(temp)<=30)):
    print ('Bring a light jacket')
else:
   print ('Do not bring a jacket')