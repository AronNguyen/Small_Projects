"""
    /**
    *Given a list of postive intergers, prints those that are perfect squares.
    *(GIGO if some of the integers are not postive)
    */
"""

def perfectSquares(x):
    for b in x:
        a = 1
        while (a * a) < b:
            a += 1
            if (a * a) == b:
                print(b, end=" ")
    print()

"""
  /**
   * Given an array of integers, returns the median (mathematically defined as
   * the middle number in sorted order if the array has odd length, or the
   * average of the two middle numbers if the array has even length).
   */
"""

def median(x):
    n = len(x)
    x.sort()
    if (n % 2) == 1:
        return x[n/2]
    else:
        return (x[n // 2 - 1] + x[n // 2]) / 2.0

## The classic "fizzbuzz" exercise.
n = 30
i = 1
for i in range(n):
    if (i % 3) == 0:
        if (i % 5) == 0:
            print("fizzbuzz")
        else:
            print("fizz")
    else:
        if(i % 5) == 0:
            print("buzz")
        else:print(i)

a, b, c = False, True, False
print(a or not(b and c))

example = [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
perfectSquares(example)
print(median(example))
