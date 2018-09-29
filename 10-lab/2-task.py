"""
    c = capacity int
    v = value array
    w = weight array
    n = number of items

    i = item number
    j = curr capacity

    PRECONDITION = weight is sorted in descending order
"""
from copy import deepcopy

def dynamicKnapsack(c, n, v, w):
    solArr = [[0]*(c+1) for _ in range(n+1)]
    keepArr = deepcopy(solArr)

    for i in range(n+1):
        for j in range(c+1):
            # if 0 items or 0 capacity
            if i == 0 or j == 0:
                pass

            # if weight of current item <= capacity
            elif w[i] <= j:
                # two options: put item or dont put item
                # value if item is taken = value of item + value at spare capacity
                val1 = v[i] + solArr[i-1][j-w[i]]
                # value if item not taken = value of row above
                val2 = solArr[i-1][j]
                # solution is max of these two
                sol = max([val1, val2])
                if sol == val1:
                    keepArr[i][j] = 1
                solArr[i][j] = sol
            else:
                solArr[i][j] = solArr[i-1][j]

    return [solArr, keepArr]

# sol, keep = dynamicKnapsack(5, 3, [0, 5, 3, 4], [0, 3, 2, 1])

# print("sol:")
# for i in sol:
#     print(i)

# print("\nkeep:")
# for i in keep:
#     print(i)