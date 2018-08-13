# Task 1a
#     Read input from user (int greater than 1582)
#     If leap year print - is a leap year
#     Else print - is not a leap year

def main():
    """ Asks for year input and prints response accordingly
    Args:
        None
    Returns:
        None
    Raises:
        No Exceptions
    Preconditions:
        None
    Complexity:
        O(1)
    """
    year = int(input("Please enter a year: "))
    if is_leap_year(year):
        print("Is a leap year")
    else:
        print("Is not a leap year")

def is_leap_year(year):
    """ Checks if a given year is a leap year
    Args:
        year (int): year to be checked
    Returns:
        True (bool): if leap year
        False (bool): if not a leap year
    Raises:
        No exceptions
    Precondition:
        year > 1582
    Complexity:
        O(1)
    """
    if (year % 100 == 0):
        if (year % 400 == 0):
            return True
        else:
            return False
    elif (year % 4 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    main()

    # if (year%400 == 0) or ((year%4 == 0) and not (year%100 == 0)):
    #     return True
    # return False