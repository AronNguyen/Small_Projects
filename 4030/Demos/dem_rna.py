
def rna_structure(rna):
    n = len(rna)
    memo = [[0] * n for i in range(n)]

    for k in range(5, n):
        for i in range(0, n - k):
            j = i + k
            memo[i][j] = memo[i][j - 1]
            for t in range(i, j - 4):
                if match(rna[t], rna[j]):
                    guess = memo[i][t - 1] + memo[t + 1][j - 1] + 1
                    if t > 0: guess += memo[i][t - 1]
                    memo[i][j] = max(memo[i][j],
                                     guess)

def match(x, y):
    return (x == 'A' and y == 'U') or 
    return memo[0][n - 1]
