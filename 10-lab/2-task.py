from copy import deepcopy

def dynamicKnapsack(c, n, v, w):
    """ Solves the knapsack problem using dynamic programming
    Args:
        c (int) = knapsack capacity
        v (list) = values os items
        w (list) = weight of items
        n (int) = number of items
    Returns:
        sol (int) = maximum value of items taken
        items (list) = items taken in knapsack in bit list form
    Raises:
        No exceptions
    Precondition:
        Weight and corresponding value must be sorted in order of descending weight
    Postcondition:
        None
    Complexity:
        O(n^2)
    """
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

    # get maximum value of solArray
    sol = max(map(max, solArr))
    items = [0]*(n+1)

    # get items in knapsack
    while n != 0:
        if keepArr[n][c] == 1:
            items[n] = 1
            c -= w[n]
            n -= 1
        else:
            n -= 1

    return [sol, items]

sol, items = dynamicKnapsack(5, 3, [0, 5, 3, 4], [0, 3, 2, 1])
print(sol, items)