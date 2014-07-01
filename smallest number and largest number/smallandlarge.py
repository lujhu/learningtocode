# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter the numbers from the book for problem 5.1 and Match the desired output as shown. 
largestnumber = None
smallestnumber = None
while True:
    entnum = raw_input("Please enter a number: ")
    if entnum == "Done":
        break
    try:
        num = int(entnum)
    except:
        print ("Please enter a numeric value")
    if largestnumber == None:
        largestnumber = num
    elif smallestnumber == None:
        smallestnumber = num
    elif num > largestnumber:
        largestnumber = num
    elif smallestnumber < num:
        smallestnumber = num
print (largestnumber, smallestnumber)  