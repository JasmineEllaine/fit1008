""" Task 3
    
    Implementing methods from task 1 using a linked structure.
"""
 
class Node:
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
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList: 
    def __init__(self, head=None):
        if head != None:
            head = Node(head)
        self.head = self.last = head

    def __str__(self):
        string = ""
        current = self.head
        while (current != None):
            string += str(current.value) + ", "
            current = current.next
        return string[:-2]

    def __len__(self):
        current = self.head
        i = 0
        while (current != None):
            i += 1
            current = current.next
        return i

    def __contains__(self, item):
        current = self.head
        while (current != None):
            if (current.value == item) and (type(current.value) == type(item)):
                return True
            current = current.next
        return False

    def __getitem__(self, index):
        i = 0
        current = self.head
        
        if index not in range(-len(self), len(self)):
            raise IndexError("Index out of range of list.")
        elif index >= 0:
            while (i < index):
                i += 1
                current = current.next
            return current.value
        elif index < 0:
            while (i < (len(self)+index)):
                i += 1
                current = current.next
            return current.value

    def __setitem__(self, index, item):
        i = 0
        current = self.head
        
        if index not in range(-len(self), len(self)):
            raise IndexError("Index out of range of list.")
        elif index >= 0:
            while (i < index):
                i += 1
                current = current.next
            current.value = item
        elif index < 0:
            while (i < (len(self)+index)):
                i += 1
                current = current.next
            current.value = item

    def __eq__(self, other):
        if len(self) == len(other):
            currentSelf = self.head
            currentOther = other.head
            i = 1
            while (i < len(self)):
                if (currentSelf.value != currentOther.value):
                # doesnt account for 1 == True
                    return False
                currentSelf = currentSelf.next
                currentOther = currentOther.next
                i += 1
            return True
        return False

    def append(self, item):
        item = Node(item)
        if (self.head == None):
            self.head, self.last = [item, item]
        else:
            self.last.next = item
            self.last = item

def linkedTestFunc():
    # str method
    aList = LinkedList()
    print(str(aList))
    bList = LinkedList(1)
    print(str(bList))
    bList.append(2)
    bList.append(3)
    print(str(bList), "\n")

    # len method
    print(len(aList))
    print(len(bList), "\n")

    # contains method
    print(1 in bList)
    print(True in bList, "\n")

    # get item method
    print(bList[2])
    print(bList[-3], "\n")
    # print(bList[3]) # error

    # set item
    bList[0] = 2
    print(str(bList))
    bList[-3] = 1
    print(str(bList), "\n")

    # eq method
    cList = bList
    print(aList == bList)
    print(bList == cList, "\n")

    # append
    print(str(aList))
    aList.append(5)
    print(str(aList))

linkedTestFunc()