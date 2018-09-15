""" Task 3
    
    Implementing methods from task 1 using a linked structure.
"""
 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

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
                