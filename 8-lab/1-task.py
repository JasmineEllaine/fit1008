from referential_array import build_array

class ArrayBasedList:
    def __init__(self, size):
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

testObject = ArrayBasedList(5)
testObject.array[0] = "hi"
testObject.array[1] = 1
testObject.array[2] = True
# print(len(testObject))
# print(str(testObject))
# print(len(testObject))
# print("hi" in testObject)

# get item test case
# print(testObject[0])
# print(testObject[-1])
# print(testObject[2])
# print(testObject[-3])
# print(testObject[3])

# set item test case
# print(testObject.array[1])
# testObject[1] = "hi"
# print(testObject.array[1])

# eq test case
# otherObject = ArrayBasedList(3)
# otherObject.array[0] = "hi"
# otherObject.array[1] = 1
# otherObject.array[2] = False
# print(testObject == otherObject)

# testObject.append("cat")
# testObject.append(2)
# print(str(testObject))
# testObject.append(False)

# testObject.insert(1, False)
# print(str(testObject) + "\n")
# # testObject.insert(0, "hello")
# testObject.insert(-4, "hello")
# print(str(testObject))

# testObject.remove("hi")
# print(str(testObject) + "\n")
# testObject.remove(True)
# print(str(testObject))
# testObject.remove("hi")

# print(str(testObject) + "\n")
# testObject.delete(2)
# print(str(testObject))

otherObject = ArrayBasedList(5)
otherObject.array[0] = 2
otherObject.array[1] = 5
otherObject.array[2] = 1
otherObject.array[3] = 4
otherObject.array[4] = 3
otherObject.sort(False)
print(str(otherObject) + "\n")
otherObject.sort(True)
print(str(otherObject))

