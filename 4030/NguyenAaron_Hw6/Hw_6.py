from heapq import heappop, heappush
"""
1a. (5, 3), (5, 2), (5, 4), (5, 1), (3, 2), (3, 1), (6, 2), (6, 4), (6, 1), (2, 1), (7, 4), (7, 1), (8, 4), (8, 1), (4, 1)
    consecutive inervsion: (5, 3), (6, 2), (8, 4), (4, 1)
"""
def find_inv(perm):

    non_con = []
    for i in range(0,len(perm)):
        for j in perm[i:]:
            if perm[i] > j and perm[i+1] != j:
                non_con.append((perm[i], j))

    if non_con:
        return non_con

    return None

"""
Its not possible to do better than n^2 becuase it has to go through the list twice
"""

print("Finding the invserions without consecutive inversions")
print(find_inv([2, 4, 1, 3, 5]))
# print(find_inv([2, 1, 4, 3, 5]))
# print(find_inv([5, 2, 4, 1, 3]))

##############################################################################

def min_delay(jobs):

    n = len(jobs)
    final_time = [None] * n
    heap = []

    for i in range(0, n):
        heappush(heap, jobs[i])

    current_time = 0
    delay = 0

    while heap:

        u = heappop(heap)
        if u > current_time:
            current_time = u
            final_time[jobs.index(u)] = u
            current_time += 10
        else:
            delay = current_time - u + delay
            final_time[jobs.index(u)] = current_time
            current_time +=10

    return (delay, final_time)

print("Finding the delay and the start time of each job")
print(min_delay([4, 32, 1, 19]))
# print(min_delay([1, 4, 19, 32]))
# print(min_delay([8, 6, 14, 12]))


"""
2b.Proof by contradiction:
    Assume that A the schdeule of jobs is not optimal
    Then the number of jobs in A is < the number of jobs in another schdeule (B)
    So in A there are k jobs while in B there are k+1 jobs
    If k+1 job in B must start after k job in B and if A's job finishes earlier
    than B's jobs then A's k job should finish before B's k job
    so A should have room to add the k+1 job from B
    This contradicts that A only has k jobs so A has to atleast as optimal as B

2c.
    Assume that the delay increase as jobs swaps but the schedule is still valid
    If Bubble sort is suppose to make B's schedule == A's schedule then the delay
    of A is == B. But this is a contradiction becuase if after every swap the delay
    increases then B will have a higher delay then A

2d. From 2b we found that the most any valid list is as good or better than any
    other list and from 2c the delay time doesnt change when swapping
    so the most optimal delay time is as good as any other schdeule
"""
