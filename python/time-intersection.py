"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """

    def timeIntersection(self, seqA, seqB):
        # Write your code here
        pts = []
        for seg in seqA + seqB:
            pts.append((seg.start, 1))
            pts.append((seg.end, -1))

        online = 0
        res = []
        lastTs = None
        for ts, delta in sorted(pts):
            if online == 2:
                self.merge(res, lastTs, ts)
            online += delta
            lastTs = ts
        return res

    def merge(self, res, start, end):
        if not start or start == end:
            return

        if res and res[-1].end == start:
            res[-1].end = end
        else:
            res.append(Interval(start, end))
