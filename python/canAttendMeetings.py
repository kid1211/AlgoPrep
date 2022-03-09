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
        sortedInt = sorted(intervals, key=lambda t: t.start)
        lastEnd = 0
        for intval in sortedInt:
            if intval.start < lastEnd:
                return False
            lastEnd = intval.end

        return True
