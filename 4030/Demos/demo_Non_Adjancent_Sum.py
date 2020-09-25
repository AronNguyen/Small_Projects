def recrusive(x):
    if len(x) == 0:
        return 0
    if len(x) == 1:
        return x[0]


    return max(recrusive(x[:-1]),
               recrusive(x[:-2]) + x[-1])

###############################################################################

def memorize(x):
    n = len(x)
    memo = [None] * (n + 1)
    memo[0] = 0
    memo[1] = x[0]
    return mem_rec(x, n, memo)


def mem_rec(x, i, memo):
    if memo[i] == None:
        memo[i] = max(mem_rec(x, i - 1, memo),
                      mem_rec(x, i - 2, memo) + x[i - 1])

    return memo[i]

###############################################################################

def dynamic_prog(x):
    n = len(x)
    memo = [None] * (n + 1)
    memo[0] = 0
    memo[1] = x[0]
    for i in range(2, n + 1):
        memo[i] = max(memo[i - 1],
                      memo[i - 2] + x[i-1])
    return memo[n]

###############################################################################

def dynamic_prog_with_sol(x):
    n = len(x)
    memo = [None] * (n + 1)
    memo[0] = 0
    memo[1] = x[0]

    choice = [None] * (n + 1)
    choice[1] = True

    for i in range(2, n + 1):
        if memo[i - 1] > memo[i - 2] + x[i - 1]:
            memo[i] = memo[i - 1]
            choice[i] = False
        else:
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

    return (memo[n], sol[::-1])

###############################################################################

print(recrusive([2, 5, 4, 8, 1, 3, 6, 9, 7]))
print(memorize([2, 5, 4, 8, 1, 3, 6, 9, 7,
                2, 5, 4, 8, 1, 3, 6, 9, 7,
                2, 5, 4, 8, 1, 3, 6, 9, 7,
                2, 5, 4, 8, 1, 3, 6, 9, 7,
                2, 5, 4, 8, 1, 3, 6, 9, 7,
                2, 5, 4, 8, 1, 3, 6, 9, 7,
                2, 5, 4, 8, 1, 3, 6, 9, 7,
                2, 5, 4, 8, 1, 3, 6, 9, 7]))
print(dynamic_prog([2, 5, 4, 8, 1, 3, 6, 9, 7]))

print(dynamic_prog_with_sol([2, 5, 4, 8, 1, 3, 6, 9, 7]))
print(dynamic_prog_with_sol([5, 2, 3, 8, 4, 3, 7, 6, 1]))
