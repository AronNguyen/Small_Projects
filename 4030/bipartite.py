"""
Using BFS for testing bipartiteness.
Author and copyright: Thomas Watson, 2019
License: For use only in COMP 4030: Design and Analysis of Algorithms,
         University of Memphis
"""

from collections import deque

def bipartite(adj):
    """
    If the given non-empty undirected graph is bipartite, returns
    (a_side, b_side) where a_side is the list of nodes on one side of some
    bipartition, and b_side is the list of nodes on the other side.
    Returns None if not bipartite.
    The graph need not be connected.
    Nodes are numbered 0,...,n-1.
    adj[u] is the list of neighbors of u.
    """

    n = len(adj)
    side = [None] * n  # None = undiscovered, 0 means a_side, 1 means b_side.
    queue = deque()

    # Try each possible starting point, to find all connected components.
    for s in range(n):
        # If s was previously discovered, then skip past it. (Otherwise we'd
        # waste time re-exploring the whole connected component containing s.)
        if side[s] != None: continue
        # Start new BFS at s. Doesn't matter which side we put it on, so we
        # arbitrarily pick a_side.
        side[s] = 0
        queue.append(s)
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if side[v] == None:
                    # The next line simultaneously marks v as discovered and
                    # puts it on the opposite side as u (since 1 - side[u]
                    # flips 0 to 1 and 1 to 0).
                    side[v] = 1 - side[u]
                    queue.append(v)
                elif side[v] == side[u]:
                    # If u and v are already in the same layer, then we know
                    # the graph contains an odd cycle so is not bipartite.
                    side[v] = 3
                    side[u] = 3

    # If we wanted a list that says for each node which side it's on, we could
    # just return the side list. But we want the list of nodes on each side,
    # and there's a slick way to get these using list comprehensions.
    a_side = [u for u in range(n) if side[u] == 0]
    b_side = [u for u in range(n) if side[u] == 1]
    c_side = [u for u in range(n) if side[u] == 3]

    output = []
    output.append(a_side)
    output.append(b_side)
    return len(output)

###############################################################################

# Here's a bipartite graph. An X means two edges, e.g., {0,3}, {1,2} are edges.
#
# 0---1
#   X
# 2---3
#   /
# 4   5
#   /
# 6---7
#   X
# 8   9

example = [[1, 3],
           [0, 2],
           [1, 3],
           [0, 2, 4],
           [3],
           [6],
           [5, 7, 9],
           [6, 8],
           [7],
           [6]]
# print(bipartite(example))
# Should return ([0, 2, 4, 5, 7, 9], [1, 3, 6, 8])
# Note that the bipartition found by our function is different than the one
# drawn above. That's fine---each connected component ({0,1,2,3,4} and
# {5,6,7,8,9} in our example) has two bipartitions (the two sides can be
# swapped), and these can be chosen independently for each component. So the
# number of possible bipartitions is 2 to the (number of connected components).
# In our example, the algorithm puts 0 on the a_side, and the first node it
# encounters in the other component is 5, which it also puts on the a_side.

# An odd cycle is not bipartite:
example2 = [[1, 4],
            [0, 2],
            [1, 3],
            [2, 4],
            [0, 3]]
# print(bipartite(example2))

example3 = [[1,6],
            [0,7],
            [8,9],
            [4,10,11],
            [3,5],
            [4,10,11],
            [0,7],
            [1,6],
            [2,9],
            [2,8],
            [3,5],
            [3,5]]
print(bipartite(example3))
