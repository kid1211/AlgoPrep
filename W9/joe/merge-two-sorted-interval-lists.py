"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """

    def mergeTwoInterval(self, list1, list2):
        # write your code here

        results = []
        idx1, idx2 = 0, 0

        while idx1 < len(list1) and idx2 < len(list2):
            if list1[idx1].start < list2[idx2].start:
                self.appendInterval(results, list1[idx1])
                idx1 += 1
            else:
                self.appendInterval(results, list2[idx2])
                idx2 += 1

        while idx1 < len(list1):
            self.appendInterval(results, list1[idx1])
            idx1 += 1

        while idx2 < len(list2):
            self.appendInterval(results, list2[idx2])
            idx2 += 1

        return results

    def appendInterval(self, results, interval):
        if len(results) == 0:
            results.append(interval)
            return

        if results[-1].end >= interval.start:
            last = results.pop()
            results.append(
                Interval(min(last.start, interval.start), max(last.end, interval.end)))
        else:
            results.append(interval)
