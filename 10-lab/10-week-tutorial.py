How to apply dynamic programming?
    1. Find the recursion in the problem.
    2. Top-down: store the answer for each subproblem in a table to avoid having to recompute them.
    3. Bottom-up: Find the right order to evaluate the resu

# TASK 1
def fib(n):
    fibMinus1 = 1
    fibMinus2 = 0

    for _ in range(2, n+1):
        fi = fibMinus1 + fibMinus2
        fibMinus1, fibMinus2 = fi, fibMinus1

    return fi

# TASK 2
Let f(n) be the maximum amount that can be picked up from
    the row of n coins. To get the recurrence for F(n),
    partition all the allowed coin selections into two 
    groups

those without the last coin
those with the last coin

Recurrence:
    # _ denotes a subscript
    F(n) = max{c_n + F(n-2), F(n-1)} for n > 1
    F(0) = 0
    F(1) = c_1

Time complexity: O(n)
Space efficiency: O(n)

def maxCoins(c):
    dp = [0]*len(c)
    dp[0] = c[0]
    dp[1] = max(c[0], c[1])
    for i in range(2, len(c)):
        dp[i] = max(dp[i-1], dp[i-2] + c[i])
    return dp[-1]

# TASK 3