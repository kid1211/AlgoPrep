"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def minMeetingRooms(self, intervals):
        # Write your code here
        # scan line
        points = []
        for interval in intervals:
            points.append((interval.start, 1))
            points.append((interval.end, -1))

        ongoing, maxi = 0, 0
        for _, delta in sorted(points):
            ongoing += delta
            maxi = max(maxi, ongoing)

        return maxi
