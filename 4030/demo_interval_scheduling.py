def interval_scheduling(intervals):
    intervals.sort(key=sort_by)

    ret = [intervals[0]]
    cur = interval[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] > cur:
            ret.appends(intervals[i])
            cur = intervals[i][1]


    return ret

def sort_by(pair):
    return pair[1]

##############################################################################

example = [(0,1),
           (0,3),
           (2,5),
           (4,6),
           (7,9),
           (0,10),
           (8,11),
           (13,14),
           (12,15)]

print(interval_scheduling(example))
