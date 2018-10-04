"""
Given as input a list of words L = [l0, l1, . . . , ln−1],
and a width M , determine what constitutes a solution to the
“justification” problem.
"""

from math import inf

def justify(l, m):
    """ Solves the text justification problem
    Args:
        l (list) = text to be justified, each word is a separate list entry
        m (list) = width of a line
    Returns:
        minCost (int) = min cost of justified text
        text (list) = indices for which text will be printed on which line
    Raises:
        No exceptions
    Precondition:
        None
    Postcondition:
        None
    Complexity:
        O(n^2)
    """
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
                costArr[i][j] = space**3

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
                possibleCosts[j] = costArr[i][j-1] + minCost[j]
                j -= 1
            minValue = min(possibleCosts.values())
            minCost[i] = minValue
            # reverse dict to get the key corresponding to min value
            reversedCosts = dict(zip(possibleCosts.values(),possibleCosts.keys()))
            text[i] = reversedCosts[minValue]
            i -= 1
            j = n-1

    return sum(minCost), text
    
def printText(l, j):
    """ Prints justified text given the indices from the justify function
    Args:
        l (list) = text to be justified, each word is a separate list entry
        j (list) = indices to be used for justification
    Returns:
        minCost (int) = min cost of justified text
        text (list) = indices for which text will be printed on which line
    Raises:
        No exceptions
    Precondition:
        None
    Postcondition:
        None
    Complexity:
        O(n^2)
    """
    i = 0
    while i < len(l):
        # print words in list starting from index, up to but not including the index given in j
        print(" ".join(l[i:j[i]]))
        i = j[i]
    
# sentence = "you can use dynamic programming to justify text and I learned that in FIT1008".split()
# minCost, textList = justify(sentence, 15)
# print(minCost)
# printText(sentence, textList)

par = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.".split()
minCost, textList = justify(par, 80)
printText(par, textList)