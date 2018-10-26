def buildArray(size):
    array = [0]*size
    print("Array built sucessfully.")
    return array

def fillArray(array):
    print("Array ")
    i = 0
    while i < len(array):
        array[i] = input("Enter element " + str(i) + ":")
        i += 1
    
def printArray(array):
    i = 0
    while i < len(array):
        print(array[i])
        i += 1

def main():
    array1 = buildArray(int(input("Enter array size: ")))
    fillArray(array1)

    array2 = buildArray(int(input("Enter array size: ")))
    fillArray(array2)

    printArray(array1)
    printArray(array2)

if __name__ == "__main__":
    main()