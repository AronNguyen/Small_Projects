"""
Intro to dynamic programming: Maximum nonadjacent sum.
Author and copyright: Thomas Watson, 2019
License: For use only in COMP 4030: Design and Analysis of Algorithms,
         University of Memphis
"""

def recursive(x):
    """
    Given a list of positive numbers, finds the maximum sum obtainable by
    adding together some of the numbers such that no two are adjacent.
    This recursive implementation takes exponential time.
    """

    # Need two base cases since the recursion will "look back" two steps.
    if len(x) == 0: return 0
    if len(x) == 1: return x[0]

    # Either don't include the last number from the list (index -1),
    #     in which case throw away the last number and recurse to get answer,
    # or do include it,
    #    in which case we get an x[-1] boost but then can't use x[-2],
    # whichever is better.
    return max(recursive(x[:-1]),
               recursive(x[:-2]) + x[-1])

###############################################################################

def memoized(x):
    """
    The above recursive function ends up solving the same subproblems over and
    over. Instead we make a "memo" list that gets the answer to each
    subproblem so we can look it up later instead of re-solving.
    """

    n = len(x)
    # memo[i] will get the max nonadjacent sum for the subproblem where we
    # only consider the first i numbers (indices 0,...,i-1). Solve the two
    # base cases directly.
    memo = [None] * (n + 1)
    memo[0] = 0
    memo[1] = x[0]

    return mem_rec(x, n, memo)

def mem_rec(x, i, memo):
    """
    x will always be the original list.
    i means we want the answer for subproblem i (using only x[0],...,x[i-1]).
    memo is the list that's passed around accumulating answers to subproblems.
    """

    # If we previously solved subproblem i, just look up the answer in memo.
    # Otherwise we have to solve subproblem i by recursing like before
    # (but now instead of passing a slice of x, we pass a reference to the
    # whole list x together with the new subproblem number).
    # Store the answer in memo[i] in case we need to look it up later.
    if memo[i] == None:
        memo[i] = max(mem_rec(x, i - 1, memo),
                      mem_rec(x, i - 2, memo) + x[i - 1])
    return memo[i]

###############################################################################

def dynamic_prog(x):
    """
    The standard way to do dynamic programming is not recursion+memoization,
    but by iteratively solving all the subproblems from smallest to biggest.
    """

    n = len(x)
    memo = [None] * (n + 1)
    memo[0] = 0
    memo[1] = x[0]

    # Simply solve each subproblem using the answers to the previous two.
    for i in range(2, n + 1):
        memo[i] = max(memo[i - 1],
                      memo[i - 2] + x[i - 1])
    return memo[n]

###############################################################################

def dynamic_prog_with_sol(x):
    """
    Returns not only the maximum sum, but also a list of indices into x
    that achieves this sum.
    """

    n = len(x)
    memo = [None] * (n + 1)
    memo[0] = 0
    memo[1] = x[0]

    # choice[i] will record which option was better when solving subproblem i:
    # True for including x[i - 1] in the sum (and thus forbidding x[i - 2]),
    # False for not including it.
    choice = [None] * (n + 1)
    choice[1] = True

    for i in range(2, n + 1):
        # If not including x[i - 1] is better:
        if memo[i - 1] > memo[i - 2] + x[i -  1]:
            memo[i] = memo[i - 1]
            choice[i] = False
        # If including x[i - 1] is better:
        else:
            memo[i] = memo[i - 2] + x[i - 1]
            choice[i] = True

    # Now construct the solution (optimal list of indices into x) by
    # "tracing back" through the choices made for each subproblem.
    sol = []
    i = n
    while i > 0:
        # If we should include index i - 1, then we should continue to find
        # the indices for solving subproblem i - 2 (indices 0,...,i-3).
        if choice[i]:
            sol.append(i - 1)
            i -= 2
        else:
            i -= 1

    # sol was constructed backward, so return the reversed version of it.
    return (memo[n], sol[::-1])

###############################################################################

example = [2, 5, 4, 8, 1, 3, 6, 9, 7]
print(recursive(example))             # Should return 26.
print(memoized(example))              # Should return 26.
print(dynamic_prog(example))          # Should return 26.
print(dynamic_prog_with_sol(example)) # Should return (26, [1, 3, 6, 8]).
