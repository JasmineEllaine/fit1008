def main():
    listSize = int(input("Enter list size: "))
    array = [0]*listSize
    index = 0
    while index < listSize:
        msg = "Enter element " + str(index) + ": "
        array[index] = int(input(msg))
        index += 1
    print("The range of this list (max-min) is", max(array)-min(array))

main()