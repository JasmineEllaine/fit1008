""" Task 3
    
    Implementing methods from task 1 using a linked structure.
"""
 
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList: 
    def __init__(self, head=None, last=None):
        self.head = head
        self.last = last

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

    def __getitem__(self, index):

def linkedTestFunc():
    # initialise list
    myList = LinkedList()

linkedTestFunc()