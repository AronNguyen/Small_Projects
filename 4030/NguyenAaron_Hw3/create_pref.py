def create_pref(a):

    man_pref = []
    woman_pref = []
    for i in range(len(a)):
        man = []
        woman = []
        for j in range(len(a)):
            x, y = a[i][j]
            man.append(x)
            woman.append(y)
        man_pref.append(man)
        woman_pref.append(woman)

    new_woman = []
    for i in range(len(woman_pref)):
        temp = []
        for j in range(len(woman_pref)):
            x = woman_pref[j][i]
            temp.append(x)
        new_woman.append(temp)


    return print(man_pref, new_woman)

create_pref([[(1, 0), (0, 1), (2, 2)],
             [(2, 1), (1, 2), (0, 1)],
             [(0, 2), (2, 0), (1, 0)]])
