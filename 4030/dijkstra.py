"""
Dijkstra's algorithm for shortest paths in graphs with positive edge lengths.
Author and copyright: Thomas Watson, 2019
License: For use only in COMP 4030: Design and Analysis of Algorithms,
         University of Memphis
"""

from heapq import heappush, heappop

def dijkstra(adj, s, t):
    """
    Given a non-empty directed graph with positive edge lengths, finds a
    shortest path from s to t. Returns a pair:
    (length of shortest path, path represented as list of node indices).
    Returns None if there is no path from s to t.
    Nodes, including s and t, are numbered 0,...,n-1.
    adj[u] is the list of pairs representing edges coming out of u:
    (l, v) means the edge from u to v has length l.
    """

    if s == t: return (0, [s])  # Special case: no edges needed.

    n = len(adj)
    # finalized[v] will become True when we know for sure the shortest path
    # distance from s to node v. At that time, dist[v] will be set to this
    # distance, and prev[v] will be set to a node u such that a shortest path
    # from s to u followed by the edge u -> v constitutes a shortest path
    # from s to v.
    finalized = [False] * n
    dist = [None] * n
    prev = [None] * n

    # Each element in the priority queue will be a tuple (d, w, v) meaning
    # that the shortest path from s to v that ends with the edge w -> v has
    # total length d. Since d is the 0-th component, the heap sorts by d.
    heap = []

    finalized[s] = True
    dist[s] = 0

    u = s
    while u != t:
        # At the start of each iteration of the loop, u is the most recently
        # finalized node. For every edge u -> v, we now know the length of a
        # shortest path to v ending with u -> v, so we add these tuples to the
        # priority queue. If v is already finalized, it's not necessary to add
        # (but wouldn't hurt if we did).
        for (l, v) in adj[u]:
            if not finalized[v]:
                heappush(heap, (dist[u] + l, u, v))
        # We search for the next node to finalize by popping from the heap
        # until we get a non-finalized v.
        u = None
        while heap:
            d, w, v = heappop(heap)
            if not finalized[v]:
                # We now know that some shortest path to v ends with w -> v
                # and has total length d, so we finalize v.
                finalized[v] = True
                dist[v] = d
                prev[v] = w
                u = v
                break
        # If the heap was exhausted without finding a non-finalized node,
        # then we've explored everything reachable from s. Since we haven't
        # found t yet, t must not be reachable.
        if u == None: return None

    # If loop terminated with u == t, then t must be reachable from s.
    # Just like in BFS, follow prev pointers to reconstruct the shortest path
    # in backward order, then reverse it.
    path = [t]
    v = t
    while v != s:
        v = prev[v]
        path.append(v)
    return (dist[t], path[::-1])

###############################################################################

# This example graph appears in section 4.4 of the Kleinberg-Tardos book but
# with nodes labeled s,u,v,x,y,z instead of 0,1,2,3,4,5.
example = [[(1, 1), (2, 2), (4, 3)],
           [(1, 3), (3, 4)],
           [(2, 3), (3, 5)],
           [(1, 4), (2, 5)],
           [],
           []]
print(dijkstra(example, 0, 5))
# Should print (4, [0, 1, 3, 5]) since that shortest path has length 1+1+2=4.
