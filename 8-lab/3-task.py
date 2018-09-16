""" Task 3
    
    Implementing methods from task 1 using a linked structure.
"""
 
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList: 
    def __init__(self, head=None):
        self.head = head
        self.last = head

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

    def append(self, item):
        if (self.head == None):
            self.head, self.last = [item, item]
        else:
            self.last.next = item
            self.last = item

def linkedTestFunc():
    # initialise nodes
    aNode = Node(1)
    bNode = Node(2)
    cNode = Node(3)

    # str method
    aList = LinkedList()
    print(str(aList))
    bList = LinkedList(aNode)
    print(str(bList))
    bList.append(bNode)
    bList.append(cNode)
    print(str(bList), "\n")

    # len method
    print(len(aList))
    print(len(bList), "\n")

    # contains method
    print(1 in bList)
    print(True in bList, "\n")

    # get item method
    print(bList[0])

linkedTestFunc()