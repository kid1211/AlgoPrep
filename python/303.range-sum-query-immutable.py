#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start


class NumArray:

    def __init__(self, nums: List[int]):
        self.maxSize = len(nums)
        self.sums = []
        curr = 0

        for num in nums:
            curr += num
            self.sums.append(curr)
        # print(self.sums)

    def sumRange(self, i: int, j: int) -> int:
        if j > self.maxSize:
            return - 1
        lowerBound = 0 if i - 1 < 0 else self.sums[i - 1]
        return self.sums[j] - lowerBound


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end
