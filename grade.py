# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message
# If the score is between 0.0 and 1.0, print a grade using the following table
# Score Grade >= 0.9 A >= 0.8 B >= 0.7 C >= 0.6 D < 0.6 F 
# Enter score: perfect Bad score
# Enter score: 10.0 Bad score
# Enter score: 0.75 C
# Enter score: 0.5 F
# USES MULTI WAY BRANCH
X = input('Enter a score between 0.0 and 1.0\n')
try:
    score = float(X)
    if score > 1:
        print('Bad Score')
    elif score >= 0.9:
        print('A')
    elif score >=0.8:
        print('B')
    elif score >=0.7:
        print('C')
    elif score >=0.6:
        print('D')
    elif score >=0.0:
        print('F')
    elif score <0.0:
        print('Bad Score')
except:
    print('Bad Score')
