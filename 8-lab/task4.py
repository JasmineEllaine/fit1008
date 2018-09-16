from referential_array import build_array
from task2 import ArrayBasedList, arrayTestFunc
from task3 import LinkedList, linkedTestFunc

def fileToArray(filename, aList):
    file  = open(filename)
    for line in file:
        aList.append(line.strip())
    file.close()

def fileToLinkedList(filename, aList):
    file = open(filename)
    for line in file:
        aList.append(line.strip())
    file.close()

array = ArrayBasedList()
fileToArray("listItems.txt", array)

linked = LinkedList()
fileToArray("listItems.txt", linked)