"""
Question 1:
Picture in folder as well
    x = [5, 2, 3, 8, 4, 3, 7, 6, 1]
    memo[0] = 0
    memo[1] = x[0]

                    memo[i-2] + x[i - 1]
                     |  |       |   \   \
    memo = [0, 5, 5, 8, 13, 13, 16, 20, 22, 22]
            | /   |         |               |
           base (i-1)     (i-1)           (i-1)

    optimal value = 22

"""

###############################################################################

def mystery_iterative(x):

    n = len(x)
    if n == 0:
        return 1
    if n == 1:
        return x[0]


    memo = [0] * (n + 1 )
    memo[0] = 1
    memo[1] = x[0]

    for i in range(1, n):
        memo[i+1] = max(memo[i] + (i + 1),
                        memo[i - 1] + (x[i] * x[i - 1]))

    return memo[n]


example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(mystery_iterative(example))

###############################################################################

def max_chips_sol(x):
    n = len(x)

    memo = [None] * (n + 1)
    memo[0] = 0
    memo[1] = x[0]

    choice = [None] * (n + 1)
    choice[1] = True

    for i in range(2, n + 1):
        if memo[1] * 3 == max_chips(x):
            break

        if memo[i - 1] >= memo[i - 2] + x[i - 1]:
            memo[i] = memo[i - 1]
            choice[i] = False
        else:
            if memo[i - 2] + 3 * x[i - 1] == max_chips(x):
                memo[i] = memo[i - 2] + 3 * x[i - 1]
                choice[i] = True
                break
            memo[i] = memo[i - 2] + x[i - 1]
            choice[i] = True

    sol = []
    i = n
    while i > 0:
        if choice[i]:
            sol.append(i - 1)
            i -= 2
        else:
            i -= 1

    return (sol[::-1])

def max_chips(x):
    n = len(x)
    memo = [None] * (n + 1)
    memo[n] = 0
    memo[n - 1] = max(0, 3 * x[n - 1])
    for i in range(n - 2, -1, -1):
        memo[i] = max(memo[i + 1],
                      memo[i + 2] + x[i],
                      3 * x[i])
    return memo[0]

# print(max_chips_sol([13, 11, 10, 14, 7, 9, 6, 5, 8, 4, 5, 3, 3, 1]))

# print(max_chips_sol([18, 17, 7, 4]))

# print(max_chips_sol([9, 8, 7, 6, 5, 4, 3, 2, 1]))

# print(max_chips_sol([13, 11, 10, 14, 17, 7,]))

###############################################################################

"""
Question 4:
Picture as well in folder
               intervals i
    ______| 0   1   2   3   4   5
    start | 0   2   7   1   4   11
    finish| 3   6   9   10  12  14
    value | 6   4   1   5   2   3

    0   v(0)=6  3
    |-----------|
            2   v(1)=4  6
            |-----------|   7    v(2)=1   9
                            |-------------|
        1               v(3)=5                 10
        |--------------------------------------|
                   4              v(4)=2               12
                   |-----------------------------------|
                                                  11   v(5)=3   14
                                                   |------------|
    P(1) = 0
    P(2) = 0
    P(3) = 2
    P(4) = 0
    P(5) = 1
    P(6) = 4

    memo[0] = 0
    memo[1] = interval[0][2]

            memo[p(i)] + v(i-1)
                     |    \   \
    memo = [0, 6, 6, 7, 7, 8, 10]
            | /   |     |
           base  (i-1) (i-1)

    optimal value = 10
"""

###############################################################################

def mining(x):
    n = len(x)

    memo = [None] * (n)
    memo2 = [None] * (n)

    memo[0] = 3 * x[0]
    memo2[0] = 2 * x[0]


    memo2[1] = max(2 * x[0], 2 * x[1])
    memo[1] = max(3 * x[1], memo2[1])

    memo2[2] = max((2 * x[2]) + memo2[0], memo[1])
    memo[2] = max(3 * x[2], memo2[2])

    for i in range(3,n):
        temp = max(memo2[i - 2],
                   memo[i - 3])

        memo2[i] = max((2 * x[i]) + temp,
                        memo[i-1])

        memo[i] = max(memo[i-3] + 3 * x[i],
                      memo2[i])

    return memo[-1]


print(mining([4, 6, 1, 4, 3, 1, 3, 2, 3, 4, 5, 6]))
