#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start


class Solution:
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        leftMax, rightMax = [], [0 for _ in range(n)]
        left, right = 0, 0

        for i in range(n):
            left = max(left, height[i])
            leftMax.append(left)
            right = max(right, height[n - i - 1])
            rightMax[n - i - 1] = right

        # print(leftMax, rightMax)
        sums = 0
        for i in range(n):
            maxheight = min(leftMax[i], rightMax[i])
            sums += maxheight - height[i]
        return sums

    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        if right < 0:
            return 0
        leftMax, rightMax = height[left], height[right]

        sums = 0
        while left <= right:
            if leftMax < rightMax:
                leftMax = max(leftMax, height[left])
                sums += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                sums += rightMax - height[right]
                right -= 1

        return sums


    # [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # (0, 0), (11, 1) -> [0]                  **    [(11,1)]
    # (1, 1), (11, 1) -> [0, 1]               **    [(11,1)]
    # (1, 1), (10, 2) -> [0, 1]               **    [(11,1), (10, 2)]
    # (2, 0), (10, 2) -> [0, 1]               **    [(11,1), (10, 2)]
    #                   [0] ->  pop 1 out, max height 1, curr 0
    #                   []  -> pop 0 out, max height 0, curr 1,
    # (2, 2), (10, 2) -> [0, 2]               **    [(11,1), (10, 2)]
    # (3, 2), (09, 1) -> [0,2]                **    [(11,1), (10, 2)] -> [(9, 1)]
    #                                               [(11,1)] -> pop 10 out, max 1, curr 1
    #                                               [] -> pop 11 out, max 0
    # (3, 2), (07, 3) ->
    # (4, 1), (07, 3) ->
    # (5, 0), (07, 3) ->
    # (6, 1), (07, 3) ->
    # **done**
# @lc code=end
0 0
1 0
2 1
3 0
4 1
5 2
6 1
7 0
8 1
9 2
10 1
11 2

# 0 0 1
# 1 1 2
# 2 1 2
# 3 2 2
# 4 2 3
# 5 2 3
# 6 2 3
# 7 3 3
# 8 3 3
# 9 3 3
# 10 3 3
# 11 3 3
