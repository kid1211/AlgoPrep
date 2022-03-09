#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        self.dfs([], 0, nums, res)
        return res

    def dfs(self, curr, index, nums, res):
        res += [list(curr)]

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            curr.append(nums[i])
            self.dfs(curr, i + 1, nums, res)
            curr.pop()

# @lc code=end
