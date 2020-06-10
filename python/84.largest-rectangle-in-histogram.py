#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # write your code here
        monStack = []
        biggest = -sys.maxsize + 1
        n = len(heights)

        if n <= 0:
            return 0

        for idx in range(n + 1):
            height = heights[idx] if idx < n else -sys.maxsize + 1

            while len(monStack) > 0 and heights[monStack[-1]] > height:
                valIdx = monStack.pop()
                lowerBound = monStack[-1] + 1 if len(monStack) > 0 else 0
                rec = heights[valIdx] * (idx - lowerBound)
                biggest = max(biggest, rec)
            monStack.append(idx)

        return biggest
# @lc code=end


215623
2 - 0
1 - 1
156 - 123
12 - 14
123 - 154

# 9 7 5 6 2 3
# lastPopedIndex = 0
# 9x1, 7x2, 5x4, 6x1, 2x6, 3x1

# # only stor the index
# [0] -> [] -> [1]
# 9 x(1 - 0)
# [1] -> [] -> [2]
# 7 x(2 - 0)
# [2] -> [2, 3]
# [2, 3] -> [3]
# 6 x(4 - (2 + 1))
# [2] -> []
# 5 x(4 - 0)
# [] -> [4]
# [4] -> [4, 5]
# [4, 5] -> [4]
# 3 x(6 - (4 + 1))
# [4] -> []
# 2 x(6 - 0)
