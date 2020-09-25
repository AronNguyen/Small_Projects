"""
Question 1:
    Find(3) = 3
    Find(6) = 6
    Union(6,7) = 0, 1, 2, 3, 4, 5, (6,7), 8, 9, 10
    Union(3,6) = 0, 1, 2, 4, 5, (3,6,7), 8, 9, 10
    Find(3) = 6
    Union(0,9) = (0,9) 1, 2, 4, 5, (3,6,7), 8, 10
    Find(9) = 0
    Union(0,6) = (0,3,6,7,9), 1, 2, 4, 5, 8, 10
    Find(9) = 6
    Union(4,8) = (0,3,6,7,9), 1, 2, (4,8), 5, 10
    Union(2,5) = (0,3,6,7,9), 1, (2,5) (4,8), 10
    Find(4) = 4
    Union(1,4) = (0,3,6,7,9), (2,5) (1,4,8), 10
    Find(5) = 2
    Union(2,4) = (0,3,6,7,9), (1,2,4,5,8), 10
    Find(1) = 4
    Union(6,10) = (0,3,6,7,9,10), (1,2,4,5,8)
    Find(5) = 4
    Union(4,6) = (0,1,2,3,4,5,6,7,8,9,10)
    Find(3) = 6
    Find(10) = 6
"""

###############################################################################
"""
Question 2a.
"""
def is_component_valid(component):
    n = len(component)
    for i in range(n):
        v = component[i]
        if component[v] != v:
            return False
    return True

temp = [1, 2, 3]
temp2 = [1, 2, 2]
temp3 = [1, 1, 2]

print(is_component_valid(temp))
print(is_component_valid(temp2))
print(is_component_valid(temp3))

###############################################################################
"""
Question 3.
    a.1101|0|10|1100|10|0
       q   r t    p  t  r
    b.(0.08 * 4) + (0.18 * 4) + (0.32 * 1) + (0.17 * 4) + (0.20 * 2) + (0.05 * 4)
        0.32 + 0.72 + 0.32 + 0.68 + 0.40 + 0.20 = 2.64
    c.
                                      (1)
                                     /   \
                                    /     \
                                   /       \
                                  /         \
                                 /           \
                                /             \
                               /               \
                            (0.62)              \
                            /    \               \
                           /      \               \
                        (0.30)  (0.32)          (0.38)
                        /    \                  /    \
                       /      \                /      \
                    (0.13)  (0.17)          (0.20)  (0.18)
                    /   \
                   /     \
                (0.08) (0.05)



"""

##############################################################################

from heapq import heappush, heappop, heapify

def unflatten(pairs):
    RightSide = pairs
    heapify(RightSide)

    LeftSide = []

    while len(RightSide) > 1:
        cdL, letterL = heappop(RightSide)
        # print(len(cdL))
        # print(letterL)
        cdR, letterR = heappop(RightSide)
        # print(letterR)
        # print(len(cdR))
        print(RightSide)
        if cdL[0:len(cdL)-1] == cdR[0:len(cdR)-1]:
            # print(RightSide)
            heappush(RightSide, (cdL[0:len(cdL)-1]  ,(letterL, letterR) ))

        else:
            heappush(LeftSide, (cdL, letterL))
            heappush(RightSide, (cdR, letterR))

        if len(LeftSide) == 2 and len(RightSide) == 1:
            cdL, letterL = heappop(LeftSide)
            cdR, letterR = heappop(LeftSide)
            heappush(RightSide, (cdL[0:len(cdL)-1]  ,(letterL, letterR) ))
            # print(RightSide)

    cd, root = heappop(RightSide)
    return root

print(unflatten([('11','a'),('010','b'),('10','c'),('00','d'),('011','e')]))
