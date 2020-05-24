#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs([], 0, result, nums)
        return result

    def dfs(self, current, index, result, nums):
        result.append(list(current))

        for i in range(index, len(nums)):
            current.append(nums[i])
            self.dfs(current, i + 1, result, nums)
            current.pop()
# @lc code=end
