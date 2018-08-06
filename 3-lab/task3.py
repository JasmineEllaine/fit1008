arraySize = int(input("Enter size: "))
array = [0]*arraySize
index = 0
while index < arraySize:
    msg = "Enter element " + str(index) + ": "
    array[index] = int(input(msg))
    index += 1

compTemp = int(input("Comparison temperature: "))
index = 0
cnt = 0
while index < arraySize:
    if array[index] > compTemp:
        cnt += 1
    index += 1

print("Temperature was exceeded", cnt, "time(s).")