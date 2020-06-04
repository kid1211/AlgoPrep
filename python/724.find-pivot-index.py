#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        curr, sums = 0, []
        for num in nums:
            curr += num
            sums += [curr]

        n = len(sums)
        for i in range(n):
            lowerBound = 0 if i == 0 else sums[i - 1]
            if lowerBound == (sums[n - 1] - sums[i]):
                return i

        return -1


# @lc code=end
[-1, -1, -1, 0, 1, 1]
