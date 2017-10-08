# Below is an extracted dataset from NSW Department of Planning and Environment showing counts of building
#  approvals and completions from previous years. Please put this in a text file. 
#  Write a program to read each record and output the total number of approvals in the Central district for year 2016.   
# Hint: To split the fields into individual tokens, statement looks like this -> fields = line.split('|')

fhand = open('NSWDOP.txt')
sum_2016 = 0
for line in fhand:
    line = line.rstrip().split('|')
    if not 'Central' in line: continue
    district = line[1]  
    appr_2016 = line[2]
    sum_2016 = float(sum_2016) + float(appr_2016)
print('The total number of approvals in 2016 for district' ,district, 'was' ,sum_2016)
