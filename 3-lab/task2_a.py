# Task 2a
#     Reads in the size of the the_list from the user
#     Reads in all the items from the user into the_list
#     Prints the range of the_list

def main():
    """ Find range of a user inputted array
    Args:
        None
    Returns:
        None
    Raises:
        No Exceptions
    Preconditions:
        None
    Complexity:
        O(n)
    """
    arraySize = int(input("Enter list size: "))
    array = buildArray(arraySize)
    arrayRange = findRange(array)
    print("The range of this list (max-min) is",arrayRange)

def buildArray(size):
    """ Creates an array of length size using user input data
    Args:
        size (int): length of the array
    Returns:
        array (list): array with length size filled with user input
    Raises:
        No Exceptions
    Preconditions:
        None
    Complexity:
        O(n)
    """
    array = [0]*size
    for i in range(size):
        msg = "Enter element " + str(i) + ": "
        array[i] = int(input(msg))
    return array

def findRange(array):
    """ Finds the range of an array
    Args:
        array (list): length of the array
    Returns:
        (int): range of the array
    Raises:
        No Exceptions
    Preconditions:
        None
    Complexity:
        O(n)
    """
    return max(array) - min(array)

if __name__ == "__main__":
    main()