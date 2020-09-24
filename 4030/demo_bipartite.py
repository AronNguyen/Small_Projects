from collections import deque
def bipartite(adj):
    n = len(adj)
    side = [None] *n
    queue = deque()

    for s in range(n):
        if side[s] != None: continue

        side[s] = 0
        queue.append(s)
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if side[v] == None:
                    side[v] = 1 - side[u]
                    queue.append(v)
                elif side[v] == side[u]:
                    side[v] = 3
                    side[u] = 3

    a_side = [u for u in range(n) if side[u] == 0]
    b_side = [u for u in range(n) if side[u] == 1]
    return (a_side, b_side)



example = [[1,3],
           [0,2],
           [1,3],
           [0,2,4],
           [3],
           [6],
           [5,7,9],
           [6,8],
           [7],
           [6]]
# print(bipartite(example))

example2 = [[1,4],
            [0,2],
            [1,3],
            [2,4],
            [0,3]]

# print(bipartite(example2))

example3 = [[1,6],
            [0,7],
            [8,9],
            [4,10,11],
            [3,5],
            [4,10,11],
            [0,7],
            [1,6],
            [2,9],
            [2,8],
            [3,5],
            [3,5]]
print(bipartite(example3))
