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
    @return: if a person could attend all meetings
    """

    def canAttendMeetings(self, intervals):
        # Write your code here

        ints = []

        for interval in intervals:
            ints.append((interval.start, 1))
            ints.append((interval.end, -1))

        overlap = 0

        for ts, delta in sorted(ints):
            if overlap > 1:
                return False
            overlap += delta
        return True


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
    @return: if a person could attend all meetings
    """

    def canAttendMeetings(self, intervals):
        # Write your code here
        lastEnd = None
        for interval in sorted(intervals, key=lambda n: n.start):
            if lastEnd and lastEnd > interval.start:
                return False
            lastEnd = interval.end

        return True
