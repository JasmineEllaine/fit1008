"""TASK 1"""

global count
count = 0

# part 1
def simpleFib(n):
    # program counter
    global count
    count += 1

    if n == 0:
        return 0
    if n == 1:
        return 1
    return simpleFib(n-1) + simpleFib(n-2)

# part 2
def fibCounter(func, n):
    global count
    count = 0
    func(n)

    # reset counter without losing value
    tmp = count
    count = 0
    return tmp

# part 3
def dynamicFib(n):
    global count

    fibMinus1 = 1
    fibMinus2 = 0

    for _ in range(2, n+1):
        fi = fibMinus1 + fibMinus2
        fibMinus1, fibMinus2 = fi, fibMinus1
        # program counter
        count += 1

    return fi

print(fibCounter(simpleFib, 8))
print(fibCounter(dynamicFib, 8))