def subheap(list, x):
    temp = []
    temp.append(list[x])
    y = x
    z = x
    for i in list:
        temp.extend(list[(2*y+1):(2*z+3)])
        y = 2*y+1
        z = 2*z+2
    print(temp)

test_heap = [1, 4, 3, 10, 9, 8, 14, 11, 18, 17, 15, 16, 13, 20, 22, 19, 21, 25, 23]
subheap(test_heap, 1)
