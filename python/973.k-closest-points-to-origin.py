#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start

from heapq import heappush, heappop


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distants = []
        # print(sqrt(-6 * -6 + -5 * -5))

        for idx, tur in enumerate(points):
            x, y = tur
            dis = sqrt(x * x + y * y)
            # print(dis)
            heappush(distants, (-dis, tur))

            # print("before", distants)
            if len(distants) > K:
                heappop(distants)

        ans = []
        while len(distants) > 0:
            _, tur = heappop(distants)
            ans.append(tur)

        ans.reverse()
        return ans


# @lc code=end
