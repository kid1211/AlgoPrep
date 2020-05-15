#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        self.helper([], 0, results, target, sorted(candidates))
        return results

    def helper(self, current, index, results, target, nums):
        if sum(current) > target:
            return
        if sum(current) == target:
            results.append(list(current))
            return

        for i in range(index, len(nums)):
            current.append(nums[i])
            # if you don't want to access youself again, do i + 1
            self.helper(current, i, results, target, nums)
            current.pop()
# @lc code=end
