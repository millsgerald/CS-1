count = 0
sum = 0
while True:  
    try:
        x = input('Enter a number\n')
        if x == 'done':
            break
        value = int(x)
        count = count+1
        sum = sum+int(value)
    except:
        print('Invalid Input')
print ('Total:',sum,'Count:',count,'Average:',sum/count)
