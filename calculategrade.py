## 3.3 Write a program to prompt the user for a score using raw_input. 
## Print out a letter grade based on the following table:
## Score Grade
## >= 0.9 A
## >= 0.8 B
## >= 0.7 C
## >= 0.6 D
## < 0.6 F
## If the user enters a value out of range, print a suitable error message and exit. 
## For the test, enter a score of 0.85
gradestring = raw_input("Please enter a grade between 0 and 1: ")
try: 
	grade = float(gradestring)
except:
    print "Bad Score"
def computegrade(x):
    if x >1:
        return "Bad Score"
    elif x >= 0.9:
        return "A"
    elif x >= 0.8:
        return "B"
    elif x >= 0.7:
        return "C"
    elif x >= 0.6:
        return "D"
    elif x >= 0:
        return "F"
    else:   
        return "Bad Score"
print computegrade(grade)		