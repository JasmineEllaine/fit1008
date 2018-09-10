from referential_array import build_array

class ArrayBasedList:

#     Modify your list implementation so that the size of the underlying array is dynamic. The base size of the
# array is 20 and should never be less than 20. However, if the list becomes full, it is resized to be 2 times
# larger than the current size. Likewise, the underlying size should decrease by half if the underlying array
# is larger than the base size but the content occupies less than 1
# 8
# of the available space. When resizing the
# list, retain the contents of the list. That is, when it is initially filled, it will be resized to 20 items, then 40,
# while retaining the contents initially in it. The same happens when the size of the array shrinks.

    def __init__(self, size):
        assert size >= 20
        self.array = build_array(size)
        self.maxSize = size

    def __str__(self):
        string = ""
        for elem in self.array:
            if elem != None:
                string += str(elem)
                string += "\n"
        return string[:-1]

    def __len__(self):
        i = 0
        while (i < self.maxSize) and (self.array[i] != None):
            i += 1
        return i
    
    def __contains__(self, item):
        for elem in self.array:
            if item == elem:
                return True
        return False

    def __getitem__(self, index):
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
                tmp2 = self.array[index:-1]
                self.array = tmp1 + [item] + tmp2
            elif index < 0:
                tmp1 = self.array[:abs(index)-1]
                tmp2 = self.array[abs(index)-1:-1]
                self.array = tmp1 + [item] + tmp2
    
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

    def sort(self, reverse):
        if reverse:
            pass
        else:
            for i in range(1, len(self.array)):
                key = self.array[i]
                j = i-1
                while j >=0 and key < self.array[j] :
                        self.array[j+1] = self.array[j]
                        j -= 1
                self.array[j+1] = key