from collections import deque
def shortest_path(adj, s, t):
    if s == t:
        #returns a length of 0
        return 0

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

                prev[v] = u
                if v == t:
                    break
                queue.append(v)

    if prev[t] == None:
        return None
    path = [t]
    v = t
    while v != s:
        v = prev[v]
        path.append(v)
        #returns the length of the path -1 to get of the starting point
    return len(path[::-1])-1


def diameter(graph):

    temp = []
    #This nested loop gives every possible outcome for the shortest path
    #between any node
    for i in range(0, len(graph)):
        for j in range(0, len(graph)):
            temp.append(shortest_path(graph,i,j))
    #max(temp) gives the maxiume of the shortest path
    return max(temp)

testing_graph =[[2,6,8,9,11,12],#0
                [2,4],#1
                [0,1],#2
                [6,7],#3
                [1, 5,10],#4
                [4,8],#5
                [0,3],#6
                [3,13],#7
                [0, 5,14],#8
                [0,13],#9
                [4,14],#10
                [0,15],#11
                [0,15,16],#12
                [7,9,16],#13
                [8,10,15],#14
                [11,12,14],#15
                [12,13]]#16

undir_example = [[1, 2],
                  [0, 2, 3, 4],
                  [0, 1, 4, 6, 7],
                  [1, 4],
                  [1, 2, 3, 5],
                  [4],
                  [2, 7],
                  [2, 6]]

print(diameter(undir_example))
# print(diameter(testing_graph))
