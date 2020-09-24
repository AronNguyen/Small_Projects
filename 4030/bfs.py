from collections import deque
def connected_bfs(adj):
    n = len(adj)
    discovered = [False] * n
    queue = deque()
    discovered[0] = True
    queue.append(0)
    how_many = 1

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not discovered[v]:
                discovered[v] = True
                queue.append(v)
                how_many += 1

    return how_many == n

###############################################################################

def strongly_connected(adj):
    n = len(adj)
    adj_rev = [[] for u in range(n)]
    for u in range(n):
        for v in adj[u]:
            adj_rev[v].append(u)

    return connected_bfs(adj) and connected_bfs(adj_rev)

###############################################################################

def shortest_path(adj, s, t):
    if s == t:
        return[s]

    n = len(adj)
    discovered = [False] * n
    queue = deque()
    prev = [None] * n

    discovered[s] = True
    queue.append(s)

    while queue and not discovered[t]:
        u = queue.popleft()
        for v in adj[u]:
            if not discovered[v]:
                discovered[v] = True
                queue.append(v)
                prev[v] = u
                if v == t:
                    break

    if prev[t] == None:
        return None
    path = [t]
    v = t
    while v != s:
        v = prev[v]
        path.append(v)
    return path[::-1]

###############################################################################

undir_example = [[1, 2],
                 [0, 2, 3, 4],
                 [0, 1, 4, 6, 7],
                 [1, 4],
                 [1, 2, 3, 5],
                 [4],
                 [2, 7],
                 [2, 6]]
print(connected_bfs(undir_example))

# dir_example = [[1],
#                [2, 3],
#                [0, 7],
#                [4],
#                [1, 2, 5],
#                [],
#                [2],
#                [6]]
#
# print(strongly_connected(dir_example))
#
# print(shortest_path(dir_example, 0, 2))
# print(shortest_path(dir_example, 3, 6))
