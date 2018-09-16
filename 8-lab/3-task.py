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

    def isEmpty(self):
        # checks if linked list is empty
        return (self.head == self.last == None)

    def __str__(self):
        string = ""
        current = self.head
        if not self.isEmpty():
            while (current.next != None):
                string += current.value + ", "
            return string[:-2]
        return string

    def __len__(self):
        current = self.head
        i = 0 if (current.next == None) else (1)
        while (current.next != None):
            i += 1
        return i

    def __contains__(self, item):
        current = self.head
        while (current != None):
            if (current.value == item) and (type(current.value) == type(item)):
                return True
            current = current.next
        return False

    # def __getitem__(self, index):

    def append(self, item):
        if (self.head == None):
            self.head, self.last = [item, item]
        else:
            self.last.next = item
            self.last = item

def linkedTestFunc():
    # initialise list
    aNode = Node(1)
    bNode = Node(2)
    cNode = Node(3)

    aList = LinkedList(aNode)
    print(str(aList))

    aList.append(bNode)
    aList.append(cNode)
    print(str(aList))

linkedTestFunc()