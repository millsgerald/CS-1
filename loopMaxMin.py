#rite another program that prompts for a list of numbers as 
#above and at the end prints out both the maximum and minimum of the numbers instead of the average.

count = 0
sum = 0
small = None
large = -1
while True:  
    try:
        x = input('Enter a number\n')
        if x == 'done':
            break
        value = int(x)
        count = count+1
        sum = sum+int(value)
        if value > large:
            large = value
        if small is None:
            small = value
        elif value < small:
            small = value
    except:
        print('Invalid Input')
print ('Total:',sum,'Count:',count,'Minimum:',small,'Maximum:',large)
