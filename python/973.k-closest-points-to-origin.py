#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start

from heapq import heappush, heappop


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            distance = sqrt(x*x + y*y)
            heappush(heap, (distance, [x, y]))

        res = []
        for _ in range(K):
            if not heap:
                return res

            _, point = heappop(heap)
            res += [point]
        return res


# @lc code=end
