# read input from user (int greater than 1582)
# if leap year print - is a leap year
# else print - is not a leap year

def main():
    year = input("Please enter a year: ")
    if is_leap_year(year):
        print("Is a leap year")
    else:
        print("Is not a leap year")

def is_leap_year(year):
    year = int(year)
    if (year%400 == 0) or ((year%4 == 0) and not (year%100 == 0)):
        return True
    return False

if __name__ == "__main__":
    main()