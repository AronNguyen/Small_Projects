def find_neg(x, z, y):
    return [i for i in x[z:y+1] if i < 0]

print(find_neg([2, -4, 3, -5, 4, -6, -7, 6, -10, 11, -1, 0], 2, 8))
