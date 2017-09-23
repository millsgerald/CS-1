# Write a program to accept the temperature value and to tell a person to bring heavy jacket if temperature is < 20, 
# if temperature is between 20 and 30, bring light jacket. if temperature > 30, do not bring any jacket.

def jacket():
    temp = 0
    while True:
        try:
            temp = int(input('Enter current temperature\n'))
            if (int(temp) < 20):
                print ('Bring a heavy jacket')
                break
            elif (int(temp) >=20 and (int(temp)<=30)):
                print ('Bring a light jacket')
                break
            else:
                print ('Do not bring a jacket')
                break
        except:
            print('Enter a valid entry')
jacket()
