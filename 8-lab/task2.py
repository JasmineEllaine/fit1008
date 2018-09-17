""" Task 2
    
    Implementing a dynamic Array Based List.
"""

from referential_array import build_array

class ArrayBasedList:
    def __init__(self):
        """ Constructor for ArrayBasedList
        Args:
            None
        Returns:
            None
        Raises:
            No exceptions
        Precondition:
            initial size of array == 20
        Postcondition:
            max size of array doubles if full, halves if contents
                occupy less than 1/8 of the max size
        Complexity:
            O(1)
        """
        self.array = build_array(20)
        self.maxSize = 20

    def increase(self):
        """ Increases the size of the array
        Args:
            None
        Returns:
            None
        Raises:
            No exceptions
        Precondition:
            maxSize > 0
        Postcondition:
            maxSize will be doubled
            array is a new array with size maxSize and its previous
                contents preserved
        Complexity:
            O(n)
        """
        self.maxSize *= 2
        tmp = self.array
        self.array = build_array(self.maxSize)
        for i in tmp:
            self.append(i)

    def decrease(self):
        """ Decreases the size of the array
        Args:
            None
        Returns:
            None
        Raises:
            No exceptions
        Precondition:
            maxSize >= 0
        Postcondition:
            maxSize will be halved
            array is a new array with size maxSize and its previous
                contents preserved
        Complexity:
            O(n)
        """
        self.maxSize //= 2
        tmp = self.array
        self.array = build_array(self.maxSize)
        for i in tmp:
            self.append(i)

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
        for elem in self.array:
            if elem != None:
                string += str(elem) + "\n"
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
        i = 0
        try: 
            while (i < self.maxSize) and (self.array[i] is not None):
                i += 1
        finally:
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
        for elem in self.array:
            if item == elem:
                return True
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
        if index not in range(-len(self), len(self)):
            raise IndexError("Index out of range of list")
        elif index >= 0:
            return self.array[index]
        elif index < 0:
            return self.array[len(self)+index]

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
        if index not in range(-len(self), len(self)):
            raise IndexError("Index out of range of list")
        elif index >= 0:
            self.array[index] = item
        elif index < 0:
            self.array[len(self)+index] = item

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
            i = 0
            while i < len(self):
                if self.array[i] != other.array[i]:
                    return False
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
            O(1) - if list is not full
            O(n) - 
        """
        if len(self) < self.maxSize:
            self.array[len(self)] = item
        else:
            self.increase()
            self.append(item)

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
        if len(self) < self.maxSize:
            if index not in range(-len(self), len(self)):
                raise IndexError("Index out of range of list")
            elif index >= 0:
                tmp1 = self.array[:index]
                tmp2 = self.array[index:]
                self.array = tmp1 + [item] + tmp2
            elif index < 0:
                tmp1 = self.array[:len(self)+index]
                tmp2 = self.array[len(self)+index:]
                self.array = tmp1 + [item] + tmp2
        else:
            self.increase()
            self.insert(index, item)
    
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
        i = 0
        while (i < len(self)):
            if (self.array[i] == item) and (type(self.array[i]) == type(item)):
                tmp1 = self.array[:i]
                if (i == len(self)-1):
                    tmp2 = []
                else:
                    tmp2 = self.array[i+1:]
                self.array = tmp1 + tmp2

                # resize list
                minSize = self.maxSize/8
                while (len(self) < minSize):
                    self.decrease()

                return None
            i += 1
        raise ValueError("Item does not exist in self")

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
        if index not in range(-len(self), len(self)):
            raise IndexError("Index out of range of list")
        elif index >= 0:
            tmp1 = self.array[:index]
            tmp2 = self.array[index+1:]
            self.array = tmp1 + tmp2
        elif index < 0:
            tmp1 = self.array[:abs(index)-1]
            tmp2 = self.array[abs(index):]
            self.array = tmp1 + tmp2
        
        # resize list
        minSize = self.maxSize/8
        while (len(self) < minSize):
            self.decrease()

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
                while j >=0 and key < self[j]:
                        self[j+1] = self[j]
                        j -= 1
                self[j+1] = key

def arrayTestFunc():
    # function to test if array is working
    # make two lists

    testObject = ArrayBasedList()
    testObject.append("hi")
    testObject.append(1)
    testObject.append(True)

    otherObject = ArrayBasedList()
    otherObject.append(2)
    otherObject.append(1)
    otherObject.append(5)
    otherObject.append(3)
    otherObject.append(4)

    # test str method
    print(str(testObject), "\n")
    print(str(otherObject), "\n")

    # len method
    print(len(testObject))
    print(len(otherObject), "\n")

    # in method
    print("hi" in testObject)
    print("hello" in testObject, "\n")

    # get item method
    print(testObject[0])
    print(testObject[-1])
    print(testObject[2])
    try:
        print(testObject[-3])
    except:
        print("Index out of range")

    try:
        print(testObject[3])
    except:
        print("Index out of range", "\n")

    # set item method
    print(testObject.array[0])
    testObject[0] = "hello"
    print(testObject.array[0], "\n")

    testObject[0] = "hi"
    print(testObject.array[0], "\n")

    # eq method
    anotherObject = ArrayBasedList()
    anotherObject.append = "hi"
    anotherObject.append = 1
    anotherObject.append = False
    print(testObject == otherObject)
    print(testObject == anotherObject, "\n")

    # append method
    testObject.append("cat")
    testObject.append(2)
    print(str(testObject))
    try:
        testObject.append(False)
    except:
        print("Array is full", "\n")

    # remove method
    testObject.remove("cat")
    testObject.remove(2)
    print(str(testObject))
    try:
        testObject.remove("cat")
    except:
        print("Item not found.", "\n")

    # insert method
    testObject.insert(1, False)
    print(str(testObject), "\n")
    testObject.insert(-4, "hello")
    print(str(testObject))
    try:
        testObject.insert(-4, "hello")
    except:
        print("Array full\n")

    # delete
    testObject.delete(-3)
    print(str(testObject), "\n")
    testObject.delete(0)
    print(str(testObject), "\n")

    otherObject.sort()
    print(str(otherObject), "\n")
    otherObject.sort(True)
    print(str(otherObject))

    # for k, v in ArrayBasedList.__dict__.items():
    # if "function" in str(v):

if __name__ == "__main__":
    arrayTestFunc()