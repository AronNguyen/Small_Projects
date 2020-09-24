def weighted_interval_scheduling(intervals):
    intervals.sort(key = sort_by)

    n = len(intervals)
    memo = [None] * (n + 1)
    memo[0] = 0
    memo[1] = intervals[0][2]

    for i in range(2, n + 1):
        l, u = 0, i - 1
        while l < u:
            m = (l + u) // 2
            if intervals[m][1] >= intervals[i -1][0]:
                u = m
            else:
                l = m + 1

        memo[i] = max(memo[i-1], memo[u] + intervals[i - 1][2])

    return memo[n]

###############################################################################

def sort_by(triple):
    return triple[1]

###############################################################################

#           S, f, V
example = [(0, 3, 2),
           (1, 5, 4),
           (4, 6, 4),
           (2, 9, 7),
           (7, 10, 2),
           (0, 11, 1)]

print(weighted_interval_scheduling(example))
