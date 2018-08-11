# Task 1b
#     Read input from user (int greater than 1582)
#     If leap year print - is a leap year
#     Else print - is not a leap year
#     No functions, to be translated to mips

year = int(input("Please enter a year: "))
if (year % 100 == 0):
    if (year % 400 == 0):
        print("Is a leap year")
    else:
        print("Is not a leap year")
elif (year % 4 == 0):
    print("Is a leap year")
else:
    print("Is not a leap year")