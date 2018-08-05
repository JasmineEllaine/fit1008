# read input from user (int greater than 1582) 
# if leap year print - is a leap year
# else print - is not a leap year
# no functions

year = int(input("Please enter a year: "))
if (year%400 == 0) or ((year%4 == 0) and not (year%100 == 0)):
    print("Is a leap year")
else:
    print("Is not a leap year")