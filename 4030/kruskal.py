"""
Kruskal's algorithm for minimum spanning trees in undirected graphs.
Author and copyright: Thomas Watson, 2019
License: For use only in COMP 4030: Design and Analysis of Algorithms,
         University of Memphis
"""

def kruskal(adj):
    """
    Given a non-empty undirected graph with edge costs (not necessarily
    positive), finds a minimum spanning tree. Returns a pair
    (total cost, list of edges) where each edge is represented as a pair
    (tuple) even though it's undirected.
    Returns None if the graph is not connected.
    Nodes are numbered 0,...,n-1.
    adj[u] is the list of pairs representing edges incident to u:
    (c, v) means the edge between u and v has cost c.
    """

    n = len(adj)

    # Get the list of all edges and sort them by cost.
    edges = []
    for u in range(n):
        for (c, v) in adj[u]:
            if u < v: edges.append((c, u, v))
    edges.sort()

    # Total cost and list of edges of the tree, which will be returned.
    total = 0
    tree = []

    # Each connected component of the tree built up so far will have one of
    # its nodes designated as the "leader"; component[u] is the index of the
    # leader of the component containing node u. Thus, component[u] ==
    # component[v] lets us check whether u and v are in the same component.
    # Initially, each node is in a component by itself.
    component = [u for u in range(n)]

    # To help us merge components, we need to tell the size of a given
    # component in O(1) time, and find all nodes in a given component in time
    # O(size of component) (without searching through all n nodes).
    # constituents[u] will be None if u is not a leader, or the list of nodes
    # in u's component if u is the leader.
    constituents = [[u] for u in range(n)]

    for (c, u, v) in edges:
        a, b = component[u], component[v]
        # Skip this edge if u, v are in the same component.
        if a == b: continue
        # Otherwise, add this edge to the MST.
        total += c
        tree.append((u, v))
        # Swap a, b if necessary so a is the leader of the bigger component.
        if len(constituents[a]) < len(constituents[b]):
            a, b = b, a
        # Merge b's component into a's: Tell all nodes in b's component that
        # their leader is now a, and update a's constituents to include b's.
        for w in constituents[b]:
            component[w] = a
        constituents[a].extend(constituents[b])
        constituents[b] = None

    if len(tree) < n - 1: return None
    return (total, tree)

###############################################################################

#     5     1
#  0-----2-----4
#  |\    |\    |
#  | \  2| \   |4
#  | 3\  |  \3 |
# 4|   \ |   \ |
#  |    \|    \|
#  1-----3-----5
#     4     3

example = [[(4, 1), (5, 2), (3, 3)],
           [(4, 0), (4, 3)],
           [(5, 0), (2, 3), (1, 4), (3, 5)],
           [(3, 0), (4, 1), (2, 2), (3, 5)],
           [(1, 2), (4, 5)],
           [(3, 2), (3, 3), (4, 4)]]
print(kruskal(example))
# Should return (13, [(2, 4), (2, 3), (0, 3), (2, 5), (0, 1)]).
# This happens to be the same MST found by our implementation of Prim, but
# the edges were added in a different order.
