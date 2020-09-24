"""
Breadth-first search.
Author and copyright: Thomas Watson, 2019
License: For use only in COMP 4030: Design and Analysis of Algorithms,
         University of Memphis
"""

from collections import deque

def connected_bfs(adj):
    """
    Determines whether a non-empty undirected graph is connected.
    Nodes are numbered 0,...,n-1.
    adj[u] is the list of neighbors of u.
    """

    n = len(adj)
    discovered = [False] * n # Keep track of which nodes have been discovered.
    queue = deque()          # Queue of nodes discovered but not yet processed.

    # Start at node 0.
    discovered[0] = True
    queue.append(0)
    how_many = 1     # Count how many nodes have been discovered.

    # BFS main loop: dequeue a node, and for each of its undiscovered
    # neighbors: mark it as discovered and enqueue it.
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not discovered[v]:
                discovered[v] = True
                queue.append(v)
                how_many += 1

    # how_many is the size of node 0's connected component; graph is connected
    # iff this is all nodes.
    return how_many == n

###############################################################################

def strongly_connected(adj):
    """
    Determines whether a non-empty directed graph is strongly connected.
    Nodes are numbered 0,...,n-1.
    adj[u] is the list of nodes to which u has an edge.
    """

    n = len(adj)
    # Reverse all the edges: v is in adj[u] iff u is in adj_rev[v].
    adj_rev = [[] for v in range(n)]
    for u in range(n):
        for v in adj[u]:
            adj_rev[v].append(u)

    # Although connected_bfs was designed for undirected graphs, if we plug
    # in a directed graph it will say whether all nodes are reachable from
    # node 0. Graph is strongly connected iff all nodes are reachable from
    # node 0 and all nodes can reach node 0 (which means reachable from node
    # 0 in the reverse graph.)
    return connected_bfs(adj) and connected_bfs(adj_rev)

###############################################################################

def shortest_path(adj, s, t):
    """
    Returns a shortest path from s to t in a non-empty directed graph.
    Returns None if there is no path from s to t.
    The path is represented as a list of node indices.
    Thus, the distance (number of edges) is len(returned list)-1.
    Nodes, including s and t, are numbered 0,...,n-1.
    adj[u] is the list of nodes to which u has an edge.
    """

    if s == t: return [s]  # Special case: path of length 0.

    n = len(adj)
    discovered = [False] * n # Keep track of which nodes have been discovered.
    queue = deque()          # Queue of nodes discovered but not yet processed.
    prev = [None] * n        # prev[v] will be node that comes before v on a
                             # shortest path from s; None if v is undiscovered.
    # Start at node s.
    discovered[s] = True
    queue.append(s)

    # BFS main loop: dequeue a node, and for each of its undiscovered
    # out-neighbors: mark it as discovered, enqueue it, and record which node
    # caused it to be discovered.
    while queue and not discovered[t]:
        u = queue.popleft()
        for v in adj[u]:
            if not discovered[v]:
                prev[v] = u
                discovered[v] = True
                if v == t: break      # Found t, no need to keep exploring.
                queue.append(v)

    # If queue became empty before finding t, then t is not reachable from s.
    if prev[t] == None: return None
    path = [t]
    v = t
    while v != s:        # Follow prev pointers to reconstruct path.
        v = prev[v]
        path.append(v)
    return path[::-1]    # Path was reconstructed backward, so reverse it.

###############################################################################

# This example graph appears in section 3.2 of the Kleinberg-Tardos book but
# with nodes numbered 1,...,8 instead of 0,...,7.
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
# print(connected_bfs(undir_example))
# Should print True.
# If we modify connected_bfs to print out the order nodes are dequeued, it
# would be 0, 1, 2, 3, 4, 6, 7, 5.

# This directed graph is like the above undirected graph, but
# the 0,1,2 triangle, the 1,3,4 triangle, and the 2,7,6 triangle have been
# oriented counter-clockwise, and the 4,2 and 4,5 edges have been oriented
# away from 4.
dir_example = [[1],
               [2, 3],
               [0, 7],
               [4],
               [1, 2, 5],
               [],
               [2],
               [6]]
# print(strongly_connected(dir_example))
# Should print False: all nodes are reachable from 0, but 0 is not reachable
# from 5.

# print(shortest_path(dir_example, 0, 2))
# Should print [0, 1, 2]. There's a longer path [0, 1, 3, 4, 2], but BFS will
# find the shortest path first.

# print(shortest_path(dir_example, 3, 6))
# Should print [3, 4, 2, 7, 6]. There's a longer path [3, 4, 1, 2, 7, 6], but
# BFS will find the shortest path first.

testing_graph =[[2,6,8,9,11,12],
                [2,4],
                [0,1],
                [6,7],
                [5,10],
                [4,8],
                [0,3],
                [3,13],
                [5,14],
                [0,13],
                [4,14],
                [0,15],
                [0,15,16],
                [9,16],
                [8,10,15],
                [11,12,14],
                [12,13]]
print(shortest_path(testing_graph, 4, 7))
