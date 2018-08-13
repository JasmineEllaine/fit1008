# Task 4a
#     Prints the frequency of each temperature in the list

def main():
    """ Prints the frequency of each temperature inputted by user
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
    arraySize = int(input("Enter list size: "))
    array = buildArray(arraySize)
    arrayMax = getMax(array, arraySize)

    bitListSize = arrayMax + 1
    bitList = makeBitList(bitListSize, arraySize, array)
    printBitList(bitListSize, bitList)

def buildArray(arraySize):
    """ Builds array of size arraySize using user input
    Args:
        arraySize (int): size of array
    Returns:
        array (list): user inputted data
    Raises:
        No Exceptions
    Preconditions:
        All items in the array must be natural numbers
    Complexity:
        O(n)
    """
    array = [0]*arraySize
    index = 0
    while (index < arraySize):
        msg = "Enter element " + str(index) + ": "
        array[index] = int(input(msg))
        index += 1
    return array

def getMax(array, arraySize):
    """ Finds the maximum value of an array
    Args:
        array (list): array of integers
        arraySize (int): size of array
    Returns:
        currMax (int): max of the array
    Raises:
        No Exceptions
    Preconditions:
        None
    Complexity:
        O(n)
    """
    index = 0
    while (index < arraySize):
        if index == 0:
            currMax = array[index]
        elif array[index] > currMax:
            currMax = array[index]
        index += 1
    return currMax

def makeBitList(bitListSize, arraySize, array):
    """ Makes a frequency list out of a temperature array
    Args:
        bitListSize (int): size of frequency list
        array (list): array of integers
        arraySize (int): size of array
    Returns:
        bitList (list): frequency list of temperatures
    Raises:
        No Exceptions
    Preconditions:
        None
    Complexity:
        O(n)
    """
    # make bitlist with length (max + 1)
    # temperature itself will be used as index since precondition
    #     states that only natural numbers can be inputted
    bitList = [0]*(bitListSize)
    index = 0
    while (index < arraySize):
        temperature = array[index]
        bitList[temperature] += 1
        index += 1
    return bitList

def printBitList(bitListSize, bitList):
    """ Prints out frequency list neatly
    Args:
        bitList (list): frequency list (integers only)
        bitListSize (int): size of frequency list
    Returns:
        Non
    Raises:
        No Exceptions
    Preconditions:
        None
    Complexity:
        O(n)
    """
    index = 0
    while (index < bitListSize):
        if bitList[index] != 0:
            print(index, "appears", bitList[index], "time(s)")
        index += 1

if __name__ == "__main__":
    main()