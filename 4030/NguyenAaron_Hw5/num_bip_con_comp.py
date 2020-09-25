from collections import deque

def num_bip_con_comp(adj):
    n = len(adj)
    side = [None] *n
    queue = deque()
    count = 0;

    for s in range(n):
        if side[s] != None: continue

        side[s] = 0
        if side[s] == 0:
            count += 1
        queue.append(s)
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if side[v] == None:
                    side[v] = 1 - side[u]
                    queue.append(v)
                elif side[v] == side[u]:
                    return count

    return count

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
print(num_bip_con_comp(example3))
