"""
Question 1:
    look at Hw9_Question_1 picture

"""

###############################################################################

def count_inversions_per(x):

    n = len(x)
    count = [0] * n
    for i in range(0, n):
        # print(x[:i+1])
        # print(sort_and_count(x[:i + 1])[1])
        count[i] = (sort_and_count(x[:i + 1])[1] - sort_and_count(x[:i])[1])

    return count

def sort_and_count(x):

    n = len(x)

    if n <= 1: return (x, 0)

    a, count_a = sort_and_count(x[:n//2])
    # print(a, count_a)
    # print(x[:n//2])
    b, count_b = sort_and_count(x[n//2:])
    # print(b, count_b)
    # print(x[n//2:])
    c, count_c = merge_and_count(a, b)
    # print(c, count_c)
    return (c, count_a + count_b + count_c)

def merge_and_count(a, b):

    merged = []
    count = 0
    l, m = len(a), len(b)
    i, j = 0, 0


    while i < l or j < m:

        if j >= m or (i < l and a[i] <= b[j]):
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
            count += l - i

    return (merged, count)

###############################################################################

example = [4, 8, 3, 2, 7, 5, 0, 9, 6, 1]

print(count_inversions_per(example))

###############################################################################
"""
Question 3:
    All in base 2
    a.[(3/4)^0 + (3/4)^1 + (3/4)^2 + ... + (3/4)^log(n)]
        The time complexity for this would be O(n) because
            the 1 is the largest number and then continues
            to decrease from there

    b.[(6/5)^0 + (6/5)^1 + (6/5)^2 + ... + (6/5)^log(n)]
        6 * c * n(1/5) = cn(6/5)^j
        6/5 = 1.2
        1.2^(log(n))
        1.2 = 2^(log(1.2))
        2^(log(1.2)(log(n)))
        (2^log(n))^log(1.2)
        n^log(1.2)
        n^(.26)

    c.  9 * c * (n/3)
        c * n * 3
        3^(log(n))
        (2^log(3))^(log(n)
        (2^log(n))^(log(3))
        n^(log(3))
        (n^log(3))^2
        n^2.5


Question 4:
60 in base 2 = 111100
21 in base 2 = 010101
x1 = 111    y1 = 101
x0 = 100    y0 = 010
(x1)(y1) = (111)(101) = 100011
(x0)(y0) = (100)(010) = 1000
(x1 + x0)(y1 + y0)

"""
