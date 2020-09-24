def dfs_recursive(adj):
    n = len(adj)
    discovered = [None] * n
    order = [0]
    discovered[0] = True
    explore(adj, 0, discovered, order)
    return order

def explore(adj, u, discovered, order):
    for v in adj[u]:
        if not discovered[v]:
            discovered[v] = True
            order.append(v)
            explore(adj, v, discovered, order)

###########################################################################

def dfs_stack(adj):
    n = len(adj)
    discovered = [None] * n
    stack = [0]

    order = []
    while stack:
        u = stack.pop()
        if not discovered[u]:
            discovered[u] = True
            order.append(u)
            for v in adj[u][::-1]:
                stack.append(v)
    return order


undir_example = [[1, 2],
                 [0, 2, 3, 4],
                 [0, 1, 4, 6, 7],
                 [1, 4],
                 [1, 2, 3, 5],
                 [4],
                 [2, 7],
                 [2, 6]]

print(dfs_recursive(undir_example))
print(dfs_stack(undir_example))
