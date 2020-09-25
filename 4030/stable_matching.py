from collections import deque
def stable_matching(n, man_pref, woman_pref):
    free = deque(range(n))
    next = [0] * n
    current = [None] * n
    ranking = [[None] * n for w in range(n)]
    for w in range(n):
        for r in range(n):
            woman_pref[w][woman_pref[w][r]] = r

    while free:
        m = free.popleft()
        w = man_pref[m][[next[m]]
        next[m] += 1
        if current[w] == None:
            current[w] = m
        else:
            mp = current[w]
            if:
                free.append(m)
            else:
                current[w] = m
                free.append(mp)

    husband = current
    wife = [None] * n
    for w in range(n):
        m = husband[w]
        wife[m] = w
    return (wife, husband)


#######################################
man_pref = [[0,1,2,3],
            [1,0,2,3],
            [3,0,1,2],
            [0,3,2,1]]

woman_pref =   [[2,0,3,1],
                [0,1,2,3],
                [3,0,2,3],
                [0,1,3,2]]

wife, husband = stable_matching(4, man_pref, woman_pref)
print(wife)
