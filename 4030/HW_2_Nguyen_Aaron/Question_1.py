import math
"""
The un-edited version made a copy of the list in x[:] and not the actual values
themselves
"""
def copy(x):

    return [x[i][:] for i in range(len(x))]

x = [[3, 5, 2, 8, 9], [1, 0, 3, 7, 2], [4, 8, 9, 3, 6]]
y = copy(x)

def odd(x):
    return [y[i][1::2] for i in range(len(y))]

def make_rect(x):
    max_len = -math.inf
    for i in range(len(x)):
        if max_len < len(x[i]):
            max_len = len(x[i])

    for i in range(len(x)):
        while len(x[i]) < max_len:
            x[i].append(None)
    return x

z = [[0, 1], [2, 3, 4, 5, 6], [7, 8, 9]]
print(make_rect(z))
print(odd(x))

"""
Qustion 2
1a. 100n = 60,000,000,000/100 = 60,000,000
1b. n^2 = 60,000,000,000**.5 = 244949
1c. n^3 = 60,000,000,000**(1/3) = 3915
1d. 2^n log 60,000,000,000 = 36
1e. 3^n log 60,000,000,000 = 23
"""
