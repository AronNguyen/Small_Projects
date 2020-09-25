"""
Interval scheduling.
Author and copyright: Thomas Watson, 2019
License: For use only in COMP 4030: Design and Analysis of Algorithms,
         University of Memphis
"""

def interval_scheduling(intervals):
    """
    Returns a largest list of intervals that are pairwise non-overlapping.
    (Touching just at an endpoint counts as overlapping.)
    intervals[i] is a tuple (left endpoint, right endpoint) of an interval.
    """

    # Sort the intervals by their right endpoint. The key=sort_by tells the
    # sort method to use our sort_by function. This sorting clobbers the
    # given intervals list (meaning the caller will be able to see that we
    # changed the list order). If we didn't want to clobber it, we could make
    # a copy before sorting.
    intervals.sort(key=sort_by)

    # Include the interval with leftmost right endpoint.
    ret = [intervals[0]]
    cur = intervals[0][1]
    # Iteratively find the next interval that doesn't overlap with the most
    # recent interval in the return list.
    for i in range(1, len(intervals)):
        if intervals[i][0] > cur:
            ret.append(intervals[i])
            cur = intervals[i][1]

    return ret

def sort_by(pair):
    """
    Since we want to sort the intervals by their right endpoint instead of
    left endpoint, this function tells the sorting method to use pair[1]
    instead of pair[0] for the sorting.
    """

    return pair[1]

###############################################################################

# This example appears in section 4.1 of the Kleinberg-Tardos book but with
# intervals indexed starting at 1 instead of 0.
example = [(0, 1),
           (0, 3),
           (2, 5),
           (4, 6),
           (7, 9),
           (0, 10),
           (8, 11),
           (13, 14),
           (12, 15)]
print(interval_scheduling(example))
# Should print [(0, 1), (2, 5), (7, 9), (13, 14)]
