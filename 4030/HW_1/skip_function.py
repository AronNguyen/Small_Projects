def skip(x):
    return [i for i in x if i not in x[::3]]

print(skip([4, 9, 7, 5, 3, 8, 2, 9, 1, 0, 17]))
