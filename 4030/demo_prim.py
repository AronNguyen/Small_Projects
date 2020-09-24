from heapq import heappush, heappop


def prim(adj):

    n = len(adj)
    finalized = [False] * n
    total = 0
    tree = []

    finalized[0] = True
    num_finalized = 1

    heap = []

    u = 0
    while num_finalized < n:
        for (c, v) in adj[u]:
            if not finalized[v]:
                heappush(heap, (c, u, v))

        u = None
        while heap:
            c, w, v = heappop(heap)
            if not finalized[v]:
                finalized[v] = True
                total  += c
                tree.append((w, v))
                num_finalized += 1
                u = v
                break
        if u == None: return None

    return (total, tree)


#############################################################################

# example = [[(1, 1), (2, 2), (4, 3)],
#            [(1, 3), (3, 4)],
#            [(2, 3), (3, 5)],
#            [(1, 4), (2, 5)],
#            [],
#            []]

example = [[(4, 1), (5, 2), (3, 3)],
           [(4, 0), (4, 3)],
           [(5, 0), (2, 3), (1, 4), (3, 5)],
           [(3,0), (4, 1), (2, 2), (3, 5)],
           [(1, 2), (4, 5)],
           [(2, 3), (3, 3), (4, 4)]]

print(prim(example))
