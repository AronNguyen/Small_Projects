"""
Depth-first search.
Author and copyright: Thomas Watson, 2019
License: For use only in COMP 4030: Design and Analysis of Algorithms,
         University of Memphis
"""

def dfs_recursive(adj):
    """
    Returns a list of node indices in the order visited by DFS in the given
    non-empty graph, starting from node 0 and processing each node's
    neighbors in the order of its adjacency list.
    Nodes are numbered 0,...,n-1.
    adj[u] is the list of neighbors of u.
    """

    n = len(adj)
    discovered = [False] * n
    order = []
    explore(adj, 0, discovered, order)
    return order

def explore(adj, u, discovered, order):
    """
    dfs_recursive sets things up, but this is the main recursive function.
    u is the index of the node to be processed.
    discovered gets passed around, recording which nodes have been processed.
    The order list gets passed around and always has the set of discovered
    nodes in the order they were marked discovered.
    """

    discovered[u] = True
    order.append(u)
    for v in adj[u]:
        if not discovered[v]:
            explore(adj, v, discovered, order)

###############################################################################

def dfs_stack(adj):
    """
    Equivalent to dfs_recursive, except it manages the stack explicitly
    rather than using the call stack.
    """

    n = len(adj)
    discovered = [False] * n
    order = []

    stack = [0]
    while stack:
        u = stack.pop()
        # u may have been pushed on the stack many times. If this is the first
        # time it's being popped, that's equivalent to when explore gets called
        # on u in dfs_recursive. Otherwise, it's equivalent to the recursive
        # version seeing u on an adjacency list but not calling explore since
        # u was already discovered.
        if not discovered[u]:
            discovered[u] = True
            order.append(u)
            # We use the reversed adjacency list so we get the same result
            # as in dfs_recursive: the 0-th entry in the adjacency list gets
            # processed first since it's added to the stack last.
            for v in adj[u][::-1]:
                stack.append(v)

    return order

###############################################################################

#       0   6
#      / \ /|
#     1---2 |
#    / \ / \|
#   3---4   7
#       |
#       5
undir_example = [[1, 2],
                  [0, 2, 3, 4],
                  [0, 1, 4, 6, 7],
                  [1, 4],
                  [1, 2, 3, 5],
                  [4],
                  [2, 7],
                  [2, 6]]
# print(dfs_recursive(undir_example))
# print(dfs_stack(undir_example))
# Both should print [0, 1, 2, 4, 3, 5, 6, 7]. If we started at a different
# node, or if we changed the order of any node's adjacency list, then the
# DFS order would be different, despite representing the same graph.
testing_graph =[[2,6,8,9,11,12],#0
                [2,4],#1
                [0,1],#2
                [6,7],#3
                [1, 5,10],#4
                [4,8],#5
                [0,3],#6
                [3,13],#7
                [0, 5,14],#8
                [0,13],#9
                [4,14],#10
                [0,15],#11
                [0,15,16],#12
                [7,9,16],#13
                [8,10,15],#14
                [11,12,14],#15
                [12,13]]#16
print(dfs_stack(testing_graph))
