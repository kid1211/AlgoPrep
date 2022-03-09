"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappush, heappop


class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """

    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        heap = []
        for idx, interval in enumerate(intervals):
            if not interval:
                continue
            start, end = interval[0].start, interval[0].end
            heappush(heap, (start, end, idx, 0))

        results = []
        while heap:
            start, end, rows, cols = heappop(heap)
            self.mergeIntervalIntoResults(results, Interval(start, end))

            if cols + 1 < len(intervals[rows]):
                nextUp = intervals[rows][cols + 1]
                heappush(heap, (nextUp.start, nextUp.end, rows, cols + 1))

        return results

    def mergeIntervalIntoResults(self, results, interval):
        if not results:
            results.append(interval)

        lastRes = results[-1]

        if lastRes.end < interval.start:
            results.append(interval)
        else:
            lastRes.end = max(lastRes.end, interval.end)
