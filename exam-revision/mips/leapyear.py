def isLeap(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    if year % 4 == 0:
        return True
    else:
        return False

def printMsg(year):
    if isLeap(year):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

def main():
    year = int(input("Enter a year: "))
    printMsg(year)

if __name__ == '__main__':
    main()