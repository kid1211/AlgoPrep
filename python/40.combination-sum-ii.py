#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        self.dfs([], 0, results, sorted(candidates), target)
        return results

    def dfs(self, current, index, results, nums, target):
        sums = sum(current)
        if sums == target:
            results.append(list(current))
            return

        if sums > target:
            return

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue

            current.append(nums[i])
            self.dfs(current, i + 1, results, nums, target)
            current.pop()


# @lc code=end
[1, 1, 2, 5, 6, 7, 10]
