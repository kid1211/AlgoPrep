"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def countOfAirplanes(self, airplanes):
        # write your code here
        plane = []
        for interval in airplanes:
            plane.append((interval.start, 1))
            plane.append((interval.end, -1))

        inSky = maxi = 0
        for _, delta in sorted(plane):
            inSky += delta
            maxi = max(maxi, inSky)

        return maxi
