
def subset_sum(w, cap):
    n = len(w)
    memo = [[0] * (cap + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for c in range(1, cap + 1):
            if w[i - 1] <= c:
                memo[i][c] = max(memo[i - 1][c],
                                 memo[i - 1][c - w[i - 1]] + w[i - 1])
            else:
                memo[i][c] = memo[i - 1][c]
    # print(memo)
    return memo[n][cap]

###############################################################################


def knapsack(w, v, cap):
    n = len(w)
    memo = [[0] * (cap + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for c in range(1, cap + 1):
            if w[i - 1] <= c:
                memo[i][c] = max(memo[i - 1][c],
                                 memo[i - 1][c - w[i - 1]] + v[i - 1])
            else:
                memo[i][c] = memo[i - 1][c]
    # print(memo)
    return memo[n][cap]

###############################################################################

print(subset_sum([2, 2, 3], 6))

print(knapsack([2, 2, 3], [10, 9, 8], 6))
