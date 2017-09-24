# Write a program to accept the temperature value and to tell a person to bring heavy jacket if temperature is < 20, 
# if temperature is between 20 and 30, bring light jacket. if temperature > 30, do not bring any jacket.

def temp(temp):
    if (temp < 20):
        return 'Bring Heavy Jacket'
    else:
        if (temp > 29):
            return 'Do not bring a jacket'
        else:
            return 'Bring a Light Jacket'
print ('temp = 15 Bring Heavy Jacket: ', temp(15))
print ('temp = 25 Bring Light Jacket: ', temp(25))
print ('temp = 30 Do not Bring a Jacket: ', temp(30))
print ('temp = -11 Bring Heavy Jacket: ', temp(-11))
