# Task 3a
#     Find how many times a given temperature is strictly exceeded
#     Read list input form user
#     Read target temperature from user

arraySize = int(input("Enter size: "))
array = [0]*arraySize
index = 0

# creates list using input from user
while index < arraySize:
    msg = "Enter element " + str(index) + ": "
    array[index] = int(input(msg))
    index += 1

compTemp = int(input("Comparison temperature: "))
index = 0
cnt = 0

# goes through the user created array and makes a tally of
#     the number of times compTemp is present
while index < arraySize:
    if array[index] > compTemp:
        cnt += 1
    index += 1

print("Temperature was exceeded", cnt, "time(s).")