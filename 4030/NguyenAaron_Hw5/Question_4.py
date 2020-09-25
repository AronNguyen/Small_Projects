from heapq import heappop, heappush
"""
4b. Worst case running time is linear O(n+m)
"""
def lex_first_topo_order(adj):
    n = len(adj)
    indeg = [0] * n
    for u in range(n):
        for v in adj[u]:
            indeg[v] += 1
    # print(indeg)

    to_delete = []
    for u in range(n):
        if indeg[u] == 0:
            heappush(to_delete, u)

    order = []
    while to_delete:
        # print(to_delete)

        u = heappop(to_delete)
        # print(to_delete)
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1

            if indeg[v] == 0:
                heappush(to_delete, v)

    if len(order) < n:
        return None

    return order

example = [[4],
           [0],
           [5],
           [1, 2],
           [],
           [4, 6],
           []]

print(lex_first_topo_order(example))
