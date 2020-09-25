def dfs_stack(adj):

    n = len(adj)
    discovered = [False] * n
    order = []
    temp = []

    stack = [0]
    temp2= [1]
    temp.append(temp2)

    while stack:
        prev = u
        u = stack.pop()

        if not discovered[u]:
            discovered[u] = True
            order.append(u)
            for v in adj[u]:
                temp.append()

            for v in adj[u][::-1]:
                stack.append(v)

    print(temp2)
    return order

undir_example = [[1, 2],
                  [0, 2, 3, 4],
                  [0, 1, 4, 6, 7],
                  [1, 4],
                  [1, 2, 3, 5],
                  [4],
                  [2, 7],
                  [2, 6]]

print(dfs_stack(undir_example))
