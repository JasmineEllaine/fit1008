""" Task 1
    
    Implementing an Array Based List and its methods.
"""

from referential_array import build_array

class ArrayBasedList:
    def __init__(self, size):
        """ Constructor for ArrayBasedList
        Args:
            size (int): maximum size of the list
        Returns:
            None
        Raises:
            No exceptions
        Precondition:
            size cannot be negative    
        Postcondition:
            len(self.array) <= size
        Complexity:
            O(1)
        """
        self.array = build_array(size)
        self.maxSize = size

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
                string += str(elem)
                string += "\n"
        return string[:-1]

    def __len__(self):
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
            bool: True for success, False otherwise.
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
            item (any): an item to be checked if in list
        Returns:
            bool: True for success, False otherwise.
        Raises:
            No exceptions
        Precondition:
            None
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
        if index not in range(-len(self), len(self)):
            raise IndexError("Index out of range of list")
        elif index >= 0:
            self.array[index] = item
        elif index < 0:
            self.array[len(self)+index] = item

    def __eq__(self, other):
        if len(self) == len(other):
            i = 0
            while i < len(self):
                if self.array[i] != other.array[i]:
                    return False
                i += 1 
            return True
        return False

    def append(self, item):
        if len(self) < self.maxSize:
            self.array[len(self)] = item
        else:
            raise IndexError("List is full")

    def insert(self, index, item):
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
            raise IndexError("List is full")
    
    def remove(self, item):
        # Deletes the first instance of item from the list. Raises a ValueError if item does
        # not exist in self
        i = 0
        while (i < len(self)):
            if (self.array[i] == item) and (type(self.array[i]) == type(item)):
                tmp1 = self.array[:i]
                if (i == len(self)-1):
                    tmp2 = []
                else:
                    tmp2 = self.array[i+1:]
                self.array = tmp1 + tmp2
                return None
            i += 1
        raise ValueError("Item does not exist in self")

    def delete(self, index):
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

    def sort(self, reverse=False):
        if reverse:
            for i in range(1, len(self.array)):
                key = self.array[i]
                j = i-1
                while j >= 0 and key > self.array[j]:
                        self.array[j+1] = self.array[j]
                        j -= 1
                self.array[j+1] = key        
        else:
            for i in range(1, len(self.array)):
                key = self.array[i]
                j = i-1
                while j >=0 and key < self.array[j] :
                        self.array[j+1] = self.array[j]
                        j -= 1
                self.array[j+1] = key

def arrayTestFunc():
    # function to test if array is working
    # make two lists

    testObject = ArrayBasedList(5)
    testObject.array[0] = "hi"
    testObject.array[1] = 1
    testObject.array[2] = True

    otherObject = ArrayBasedList(5)
    otherObject.array[0] = 2
    otherObject.array[1] = 1
    otherObject.array[2] = 5
    otherObject.array[3] = 3
    otherObject.array[4] = 4

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
    anotherObject = ArrayBasedList(3)
    anotherObject.array[0] = "hi"
    anotherObject.array[1] = 1
    anotherObject.array[2] = False
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