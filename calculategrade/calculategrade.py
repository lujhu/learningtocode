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
grade = float(gradestring)
if grade >1:
    print "Please enter a grade within the proper range"
elif grade >= 0.9:
    print "A"
elif grade >= 0.8:
    print "B"
elif grade >= 0.7:
    print "C"
elif grade >= 0.6:
    print "D"
elif grade >= 0:
   print "F"
else:   
    print "Please enter a grade within the proper range"