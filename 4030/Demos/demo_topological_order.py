def topo_order(adj):
    n = len(adj)
    indeg = [0] * n
    for u in range(n):
        for v in adj[u]:
            indeg[v] += 1


    to_delete = [u for u in range(n) if indeg[u] == 0]

    order = []
    while to_delete:
        u = to_delete.pop()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                to_delete.append(v)

    return order
example = [[3, 4, 5],
           [2, 4, 5],
           [3, 4],
           [4],
           [5, 6],
           [6],
           []]

print(topo_order(example))
