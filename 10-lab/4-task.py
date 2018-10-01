"""
Given as input a list of words L = [l0, l1, . . . , ln−1],
and a width M , determine what constitutes a solution to the
“justification” problem.
"""

from math import inf

def justify(l, m):
    # len of list
    n = len(l)
    costArr = [[0]*n for _ in range(n)]

    # fill in table with cost of storing words from l[i] to l[j]
    for i in range(n):
        for j in range(i, n):
            # get number of empty spaces if words l[i] to l[j] was stored, then cube it
            wordsUsed = l[i:j+1]
            space = m - (len("".join(wordsUsed)) + len(wordsUsed) - 1)
            # inf cost if space is negative
            if space < 0:
                costArr[i][j] = inf
            else:
                costArr[i][j] = space**2

    minCost = ["null"]*(n)
    text = ["null"]*(n)

    # find min cost and final text
    i, j = [n-1, n-1]
    while i > -1:
        # get cost of words from list[i:j+1]
        cost = costArr[i][j]
        
        if cost != inf:
            minCost[i] = cost
            text[i] = j+1
            i -= 1
        else:
            possibleCosts = {}
            while j > i:
                possibleCosts[j] = costArr[i][j-1] + costArr[j][n-1]
                j -= 1
            index = min(possibleCosts)
            minCost[i] = possibleCosts[index]
            text[i] = index
            i -= 1
            j = n-1

    return minCost, text
    
minCostList, textList = justify("Tushar roy likes to code".split(), 10)
print(minCostList)
print(textList)