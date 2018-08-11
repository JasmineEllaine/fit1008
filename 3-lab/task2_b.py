# Task 2b
#     Reads in the size of the the_list from the user
#     Reads in all the items from the user into the_list
#     Prints the range of the_list
#     No functions, to be translated to mips

arraySize = int(input("Enter list size: "))
array = [0]*arraySize

index = 0
while index < arraySize:
    msg = "Enter element " + str(index) + ": "
    array[index] = int(input(msg))

    if index == 0:
        currMax = array[0]
        currMin = array[0]
    else:
        if array[index] > currMax:
            currMax = array[index]
        if array[index] < currMin:
            currMin = array[index]
    index += 1

print("The range of this list (max-min) is", currMax-currMin)