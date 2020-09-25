def min_penalty(x, d, e):

    n = len(x)

    memo = [[None] * (e + 1) for i in range(n)]
    for b in range(e + 1):
        memo[n - 1][b] = 0
    for i in range(n - 2, -1, -1):
        if x[i]:


        else:
            memo[i][b] = memo[i + 1][b]













###############################################################################
