# check how many unique frequencies

sample = [26, 18, 22, 20, 13, 22, 19, 22, 20, 27, 18, 24, 15, 28, 26, 27, 20, 21, 23, 24, 27, 26, 15,
23, 22, 20, 23, 17, 18, 18]

# check each number in list to see if it is not in unique
unique = []

# gets list of all numbers that are unique
indexSample = 0
while indexSample < len(sample):
    if sample[indexSample] not in unique:
        unique.append(sample[indexSample])
    indexSample += 1

# counts occurencse of each item in unique
bitList = [0]*len(unique)
indexUnique = 0
indexSample = 0
while indexUnique < len(unique):
    while indexSample < len(sample):
        if unique[indexUnique] == sample[indexSample]:
            bitList[indexUnique] += 1
        indexSample += 1
    indexUnique += 1
    indexSample = 0

print(unique)
print(bitList)




# gets list of all numbers that are unique
indexSample = 0
indexUnique = 0
while indexSample < len(sample):
    if sample[indexSample] not in unique:
        unique.append(sample[indexSample])
    indexSample += 1 