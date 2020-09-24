import pprint
def min_penalty(x, d, e):

    pp = pprint.PrettyPrinter(indent=4)
    n = len(x)

    memo = [[0] * (n + 1) for i in range(e + 1)]
    for i in range(1, e + 1):
        memo[1][i] = 1 if x[i - 1] else 0


    pp.pprint(memo)
    return -1




###############################################################################

print(min_penalty([True,False, True, True, True, False, True, False, True, False], 3, 2))
