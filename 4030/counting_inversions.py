"""
Mergesort and counting inversions in permutations.
Author and copyright: Thomas Watson, 2019
License: For use only in COMP 4030: Design and Analysis of Algorithms,
         University of Memphis
"""

def mergesort(x):
    """
    Returns the sorted version of the list x.
    """

    n = len(x)
    if n <= 1: return x

    # Recursively sort the left and right halves, then merge them.
    return merge_sorted(mergesort(x[:n//2]), mergesort(x[n//2:]))

def merge_sorted(a, b):
    """
    Copied from warmup.py. Merges two sorted lists.
    """

    merged = []
    l, m = len(a), len(b)
    i, j = 0, 0
    while i < l or j < m:
        if j >= m or (i < l and a[i] <= b[j]):
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    return merged

###############################################################################

def count_inversions(x):
    """
    Returns the number of inversions in the list of numbers x (i.e., the
    number of pairs i<j such that x[i] > x[j]).
    """

    return sort_and_count(x)[1]

def sort_and_count(x):
    """
    To count inversions, it helps to sort in the process. This helper function
    returns the pair (sorted version of x, number of inversions in x).
    """

    n = len(x)
    if n <= 1: return (x, 0)

    # Recurse on the left and right halves, in the process getting the
    # number of inversions contained in each half. Then while merging, count
    # the number of inversions "across halves" (i.e., bigger number in the
    # left half, smaller number in the right half).
    a, count_a = sort_and_count(x[:n//2])
    b, count_b = sort_and_count(x[n//2:])
    c, count_c = merge_and_count(a, b)
    return (c, count_a + count_b + count_c)

def merge_and_count(a, b):
    """
    Given two sorted lists, returns the following pair:
    (merged list, number of pairs i and j such that a[i] > b[j])
    """

    merged = []
    count = 0
    l, m = len(a), len(b)
    i, j = 0, 0
    while i < l or j < m:
        # Append the smaller of a[i] and b[j] to the result, and advance the
        # corresponding index. If b[j] is smaller, then it's smaller than
        # all remaining entries of list a (namely, a[i],a[i+1],...,a[l-1])
        # so it participates in l - i many inversions.
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
print(mergesort(example))
# Should print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].

print(count_inversions([2, 4, 1, 3, 5]))
# Should print 3.
# (2 comes before before 1; 4 comes before 1; 4 comes before 3)

print(count_inversions(example))
# Should print 25.
