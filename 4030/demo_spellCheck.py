
def edit_distance(x, y, alpha, delta):

    m, n = len(x), len(y)
    memo = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1): memo[i][0] = i * delta
    for j in range(n + 1): memo[0][j] = j * delta

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            mismatch = alpha if x[i - 1] != y[j - 1] else 0
            memo[i][j] = min(memo[i - 1][j - 1] + mismatch,#substitution
                             memo[i][j - 1] + delta,#insertion
                             memo[i - 1][j] + delta)#deletion

    return memo[m][n]



print(edit_distance("ocurrance", "occurrence", 1, 3))
