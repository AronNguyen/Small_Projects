from collections import deque

def solve(maze, a, b, c, d):
    if a == c and b == d:
        return -1

    n = len(maze[0])
    discovered = [[False] * n for i in range(len(maze))]
    queue = deque()
    prev = [None] * n

    queue.append((a,b))

    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if maze[i][j] == 'X':
                discovered[i][j] = True

    while queue and not discovered[c][d]:
        u,w = queue.popleft()
        for v in range(0, len(discovered[u])):
            if discovered[u][v]:
                queue.append((u-1, v))
                break
            else:
                discovered[u][v] = True
                queue.append((u,v))
                prev[v] = (u, v)
                if u == c and v == d:
                    break
    return discovered


maze = [[' ',' ',' ',' ',' ','X',' '],#0
        [' ','X',' ','X',' ',' ',' '],#1
        [' ',' ',' ',' ','X',' ','X'],#2
        ['X',' ','X',' ','X',' ',' '],#3
        ['X',' ','X',' ','X','X',' '],#4
        [' ',' ','X',' ',' ',' ',' ']]#5
        #0  #1  #2  #3  #4  #5  #6

print(solve(maze, 5, 0, 0, 6))
