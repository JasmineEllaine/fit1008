# Task 4a
#     Prints the frequency of each temperature in the list

# get input for array
arraySize = int(input("Enter list size: "))
array = [0]*arraySize
index = 0

# build array while getting the max value at the same time
while index < arraySize:
    msg = "Enter element " + str(index) + ": "
    array[index] = int(input(msg))

    # getting max value of array
    if index == 0:
        currMax = array[0]
    else:
        if array[index] > currMax:
            currMax = array[index]
    index += 1

# make bitlist with length (max + 1)
# temperature itself will be used as index since precondition
#     states that only natural numbers can be inputted
bitList = [0]*(currMax + 1)

# counts occurences of each item and stores data in bitList
index = 0 
while (index < len(array)):
    temperature = array[index]
    bitList[temperature] += 1
    index += 1

# prints temperature frequency neatly
index = 0
while (index < len(bitList)):
    if bitList[index] != 0:
        print(index, "appears", bitList[index], "time(s)")
    index += 1