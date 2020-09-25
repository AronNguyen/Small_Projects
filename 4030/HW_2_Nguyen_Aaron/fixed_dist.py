def fixed_dist(a, b, d):
    a.sort()
    b.sort()
    x = False

    for i in range(len(b)):
        for j in range(len(a)):
            if a[j] -b[i] == d:
                print(a[j], b[i])
                x = True
    
    if x == False:
        return print(None)

fixed_dist([1, 6, 14, 22, 29], [1, 10, 13, 17, 19, 21], 5)
