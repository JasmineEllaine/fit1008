from referential_array import build_array
from task2 import ArrayBasedList, arrayTestFunc
from task3 import LinkedList, linkedTestFunc

def fileToArray(filename, aList):
    """ Reads filename into aList
    Args:
        filename (str): name of file to be read
        aList(ArrayBasedList): list where file is to be written
    Returns:
        None
    Raises:
        None
    Precondition:
        None
    Postcondition:
        file will be written into aList
    Complexity:
        O(n)
    """
    file  = open(filename)
    for line in file:
        aList.append(line.strip())
    file.close()

def fileToLinkedList(filename, aList):
    """ Reads filename into aList
    Args:
        filename (str): name of file to be read
        aList(LinkedList): list where file is to be written
    Returns:
        None
    Raises:
        None
    Precondition:
        None
    Postcondition:
        file will be written into aList
    Complexity:
        O(n)
    """
    file = open(filename)
    for line in file:
        aList.append(line.strip())
    file.close()

array = ArrayBasedList()
fileToArray("listItems.txt", array)

linked = LinkedList()
fileToArray("listItems.txt", linked)