# Go to www.data.gov.au or https://data.nsw.gov.au/, get any small dataset, convert it to text file and write
#  a program to just do a very simple read of each record in the file, some level of processing of your choice
#  (does not need to be complicated) and output a new file.

# File NSW Public Schools.
# Extract the total number of students for Secondary Schools only.

fhand = open('NSW-Public-Schools.csv')
student_num = 0
for line in fhand:
    line = line.rstrip().split(',')
    if not 'Secondary School' in line: continue
    school = line[10]
    student_number = line[6]
    try:
        student_num = float(student_num) + float(student_number)
    except:
        continue
#print(school,student_num)
    print(line[10],line[6])
