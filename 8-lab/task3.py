""" Task 3
    
    Implementing methods from task 1 using a linked structure.
"""
 
class Node:
    def __init__(self, value=None, next=None):
        """ Node constructor
        Args:
            value (any): value of node
            next (Node): next node
        Precondition:
            None
        Postcondition:
            Node is initilialised
        Complexity:
            O(1)
        """
        self.value = value
        self.next = next

class LinkedList: 
    def __init__(self, head=None):
        """ Constructor for LinkedList
        Args:
            head (Node): optional
        Returns:
            None
        Raises:
            No exceptions
        Precondition:
            None
        Postcondition:
            None
        Complexity:
            O(1)
        """
        self.head = Node(head) if (head != None) else head

    def __str__(self):
        """ Gets string representation of self
        Args:
            None
        Returns:
            string (str): string representation of self
        Raises:
            No exceptions
        Precondition:
            None
        Postcondition:
            None
        Complexity:
            O(n)
        """
        string = ""
        current = self.head
        while (current != None):
            string += str(current.value) + "\n"
            current = current.next
        return string[:-1]

    def __len__(self):
        """ Gets len of self.array
        Args:
            None
        Returns:
            i (int): len of self
        Raises:
            No exceptions
        Precondition:
            None
        Postcondition:
            None
        Complexity:
            O(n)
        """
        current = self.head
        i = 0
        while (current != None):
            i += 1
            current = current.next
        return i

    def __contains__(self, item):
        """ Checks if item is in self
        Args:
            item (any): an item to be checked if in list
        Returns:
            bool: True if item in self, False otherwise.
        Raises:
            No exceptions
        Precondition:
            None
        Postcondition:
            None
        Complexity:
            O(n)
        """
        current = self.head
        while (current != None):
            if (current.value == item) and (type(current.value) == type(item)):
                return True
            current = current.next
        return False

    def __getitem__(self, index):
        """ Returns the item at a given index
        Args:
            index (int): the index from which the item will be returned
        Returns:
            the return value (any): item at self.array[index]
        Raises:
            IndexError: if index is not in range of -len(self) and len(self)
        Precondition:
            index must be in range as stated in raises above
        Postcondition:
            None
        Complexity:
            O(n)
        """
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
        """ Returns the item at a given index
        Args:
            index (int): the index from which the item will be returned
        Returns:
            the return value (any): item at self.array[index]
        Raises:
            IndexError: if index is not in range of -len(self) and len(self)
        Precondition:
            index must be in range as stated in raises above
        Postcondition:
            None
        Complexity:
            O(1)
        """
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
        """ Checks if self is equivalent to other
        Args:
            other (ArrayBasedList): the object to be compared against
        Returns:
            bool: True if equivalent, False otherwise.
        Raises:
            None
        Precondition:
            None
        Postcondition:
            None
        Complexity:
            O(n)
        """
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
        """ Adds item to the end of self.array
        Args:
            item (any): the object to be appended
        Returns:
            None
        Raises:
            None
        Precondition:
            None
        Postcondition:
            item will be appended to list
        Complexity:
            O(1)
        """
        item = Node(item)
        if (self.head == None):
            self.head = item
        else:
            curr = self.head
            while (curr.next != None):
                curr = curr.next
            curr.next = item

    def insert(self, index, item):
        """ Inserts item in the index given
        Args:
            item (any): the object to be inserted
            index (any): index where item will be inserted
        Returns:
            None
        Raises:
            IndexError: if index is not in range(-len(self), len(self))
        Precondition:
            index is in range
        Postcondition:
            item will be inserted to list
        Complexity:
            O(1) – if list is not full before inserting
            O(n) – if list is full before inserting
        """
        i = 0
        current = self.head
        item = Node(item)

        if index not in range(-len(self), len(self)+1):
            raise IndexError("Cannot be inserted in this index.")
        elif index >= 0:
            while (i < index-1):
                i += 1
                current = current.next
            if (index == 0):
                item.next = self.head
                self.head = item
            else:
                item.next = current.next
                current.next = item
        elif index < 0:
            while (i < (len(self)+index-1)):
                i += 1
                current = current.next
            if (index == 0) or (index == -(len(self))):
                item.next = self.head
                self.head = item
            else:
                item.next = current.next
                current.next = item

    def remove(self, item):
        """ Deletes the first instance of item from the list
        Args:
            item (any): the object to be deleted
        Returns:
            None: if removing item is successful
        Raises:
            ValueError: if item does not exist in self
        Precondition:
            item exists in self
        Postcondition:
            item will be removed from list
        Complexity:
            O(n^2)  - if list occupies 1/8 of the allocated space
                before removing item
            O(n)    - all other times
        """
        curr = prev = self.head
        while (curr != None):
            if (curr == self.head):
                self.head = curr.next
                return item
            if (curr.value == item) and (type(curr.value) == type(item)):
                prev.next = curr.next
                return item
            prev = curr
            curr = curr.next

    def delete(self, index):
        """ Deletes item at a given index
        Args:
            index (int): the index where item will be deleted
        Returns:
            None
        Raises:
            IndexError: if index is not in range(-len(self), len(self))
        Precondition:
            index is in range
        Postcondition:
            item will be deleted from list
        Complexity:
            O(n) - if list occupies 1/8 of the allocated space
                before removing item
            O(1) - if no list resizing needed
        """
        i = 0
        curr = self.head

        if index not in range(-len(self), len(self)):
            raise IndexError("Cannot be deleted")
        elif index >= 0:
            while (i < index-1):
                i += 1
                curr = curr.next
            if (index == 0):
                self.head = curr.next
            else:
                curr.next = curr.next.next
        elif index < 0:
            while (i < (len(self)+index-1)):
                i += 1
                curr = curr.next
            if (index == 0) or (index == -(len(self))):
                self.head = curr.next
            else:
                curr.next = curr.next.next

    def sort(self, reverse=False):
        """ Sorts a list in ascending or descending order
        Args:
            reverse (bool): optional, states how list is to be sorted
        Returns:
            None
        Raises:
            None
        Precondition:
            list contains objects that are comparable
        Postcondition:
            list will be sorted in eitehr ascending or descending order
        Complexity:
            O(n^2) - if array is sorted in the reverse order that
                it is to be sorted
            o(n)   - all other times 
        """
        if reverse:
            for i in range(1, len(self)):
                key = self[i]
                j = i-1
                while j >= 0 and key > self[j]:
                        self[j+1] = self[j]
                        j -= 1
                self[j+1] = key        
        else:
            for i in range(1, len(self)):
                key = self[i]
                j = i-1
                while j >= 0 and key < self[j]:
                        self[j+1] = self[j]
                        j -= 1
                self[j+1] = key   

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
    aList.append(5)
    print(str(aList), "\n")

    # insert
    print(str(bList))
    bList.insert(0, 0)
    print(bList)
    bList.insert(-4, 5)
    print(bList)

    # remove
    bList.remove(0)
    print(bList, "\n")

    # delete
    bList.delete(0)
    print(bList)
    bList.delete(-1)
    print(bList, "\n")

    # sort
    bList.append(0)
    bList.append(4)
    bList.append(3)

    print(bList)
    bList.sort()
    print(bList)
    bList.sort(True)
    print(bList)

    # iterable
    for i in bList:
        print(i)

if __name__ == "__main__":
    linkedTestFunc()