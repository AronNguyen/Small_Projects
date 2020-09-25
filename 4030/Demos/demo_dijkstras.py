from heapq import heappush, heappop


def dijkstras(adj, s, t):
    if s == t: return (0, [s])

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
        if u == None: return None

    path = [t]
    v = t
    while v != s:
        v = prev[v]
        path.append(v)
    return (dist[t], path[::-1])


#############################################################################

example = [[(1, 1), (2, 2), (4, 3)],
           [(1, 3), (3, 4)],
           [(2, 3), (3, 5)],
           [(1, 4), (2, 5)],
           [],
           []]

print(dijkstras(example, 0, 5))
