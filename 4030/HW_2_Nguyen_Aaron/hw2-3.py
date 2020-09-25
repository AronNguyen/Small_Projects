"""
3a.It checks to see if the list is in accending order
3b.Big O of n^2
"""
def mystery_func(x):
    n = len(x)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if x[j] - x[i] < j - i: return False
    return True

def test(x):
    for i in range(len(x)-1):
        if (x[i + 1] - x[i]) < 0:
            return False
    return True

print(mystery_func([2,1,3,4,5,6]))
print(test([2,1,3,4,5,6]))
