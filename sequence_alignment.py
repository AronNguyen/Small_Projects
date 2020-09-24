"""
Sequence alignment (edit distance).
Author and copyright: Thomas Watson, 2019
License: For use only in COMP 4030: Design and Analysis of Algorithms,
         University of Memphis
"""

def edit_distance(x, y, alpha, delta):
    """
    Returns the minimum cost of converting string x to string y, where
    substitutions are charged alpha >= 0, and insertions and deletions are
    charged delta >= 0. Could be modified to return a solution by
    "tracing back" through the optimal choices at each step.
    """

    m, n = len(x), len(y)

    # memo[i][j] will get the edit distance for the subproblem on the first
    # i characters of x (indices 0...i-1) and the first j characters of y
    # (indices 0,...,j-1).
    memo = [[None] * (n + 1) for i in range(m + 1)]

    # If j == 0, the only possibility is i deletions.
    for i in range(m + 1): memo[i][0] = i * delta
    # If i == 0, the only possibility is j insertions.
    for j in range(n + 1): memo[0][j] = j * delta

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            mismatch = alpha if x[i - 1] != y[j - 1] else 0
            memo[i][j] = min(memo[i - 1][j - 1] + mismatch, # x[i] --> y[j].
                             memo[i - 1][j] + delta,        # x[i] is deleted.
                             memo[i][j - 1] + delta)        # y[j] is inserted.
    return memo[m][n]

###############################################################################

# print(edit_distance("ocurrance", "occurrence", 1, 3))
# Should print 4, since it's optimal to insert c and substitute e for a.

# print(edit_distance("ocurrance", "occurrence", 3, 1))
# Should print 3, since it's optimal to insert c and e and delete a.

# print(edit_distance("act", "tap", 3, 2))
# Should print 7, since it's optimal to insert t, delete c, and substitute p for t.
#                                  (Or: insert t, substitute p for c, and delete t.)


print(edit_distance("team", "mat", 5, 3))
