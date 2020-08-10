from heapq import heappush, heappop


class Solution:
    """
    @param sticks: the length of sticks
    @return: Minimum Cost to Connect Sticks
    """

    def MinimumCost(self, sticks):
        if not sticks:
            return 0

        heap = []
        for stick in sticks:
            heappush(heap, stick)

        res = 0
        while len(heap) > 1:
            current = heappop(heap) + heappop(heap)
            res += current
            heappush(heap, current)

        return res
