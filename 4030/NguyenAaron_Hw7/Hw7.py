"""
# QUESTION 1:
      egde(u,v) distance
        (0,1)     1
        (0,2)     3
        (0,3)     2
        (0,4)     10
        (0,5)     4
        (0,6)     6
        (0,7)     6
        (0,8)     12
        (0,9)     10
        (0,10)    5
        (0,11)    9
        (0,12)    12
        (0,13)    11
        (0,14)    8
        (0,15)    13
        (0,16)    13

"""

###############################################################################



from heapq import heappush, heappop

def dijkstras(adj, s, t):
    if s == t:
        # return (0, [s])
        return 0

    n = len(adj)
    finalized = [False] * n
    dist = [None] * n
    prev = [None] * n

    finalized[s] = True
    dist[s] = 0

    heap = []

    u = s
    while u != t:
        for (l, v) in adj[u]:
            if not finalized[v]:
                heappush(heap, (dist[u] + l, u, v))

        u = None
        while heap:
            d, w, v = heappop(heap)
            if not finalized[v]:
                finalized[v] = True
                dist[v] = d
                prev[v] = w
                u = v
                break
        if u == None: return 0

    path = [t]
    v = t
    while v != s:
        v = prev[v]
        path.append(v)
    # return (dist[t], path[::-1])
    return dist[t]

#############################################################################

def pickhub(adj):
    total = 0
    dist = []
    for i in range(0, len(adj)):
        for j in range(0, len(adj)):
            # print(dijkstras(adj, i, j))
            if len(adj[j]) == 0:
                break
            total += dijkstras(adj, i, j)
        dist.append(total)
        total = 0
        # print(dist)
    # print(dist)
    x = min(dist)
    y = dist.index(x)
    return (y, x/len(adj))


# example = [[(1, 1), (2, 2), (4, 3)],
#            [(1, 3), (3, 4)],
#            [(2, 3), (3, 5)],
#            [(1, 4), (2, 5)],
#            [],
#            []]

example = [[(4, 1), (5, 2), (3, 3)],
           [(4, 0), (4, 3)],
           [(5, 0), (2, 3), (1, 4), (3, 5)],
           [(3, 0), (4, 1), (2, 2), (3, 5)],
           [(1, 2), (4, 5)],
           [(3, 2), (3, 3), (4, 4)]]

print('Question 2')
# print(dijkstras(example, 0, 5))
print(pickhub(example))

###############################################################################

"""
Question 3:
    (u, v)     edges
    (0, 1)      1
    (1, 2)      2
    (2, 5)      1
    (0, 3)      2
    (3,10)      3
    (10, 7)     1
    (7, 14)     1
    (14, 11)    1
    (11, 14)    1
    (11, 8)     3
    (8, 15)     2
    (8, 12)     1
    (12, 16)    1
    (16, 13)    2
    (13, 9)     1
    (2, 6)      3
    total cost = 26
"""

################################################################################

def is_valid_cut(n, X, S):

    edges = []

    for u in X:
        edges.append(u)

    for i in range(n+1):
        if edges[i][0] in S:
            return False
        if edges[i][1] in S:
            return False

    return True

x = [(0,1),
    (0,2),
    (2,0),
    (1,0),
    (1,3),
    (2,5)]

s = [5,7,8,9,10]
print('Question 4')
print(is_valid_cut(5, x, s))
