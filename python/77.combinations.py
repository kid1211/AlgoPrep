#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        # do k after
        results = []
        self.dfs([], 0, results, nums, k)
        return results

    def dfs(self, current, index, results, nums, k):
        if len(current) == k:
            results.append(list(current))
            return

        for i in range(index, len(nums)):
            current.append(nums[i])
            self.dfs(current, i + 1, results, nums, k)
            current.pop()


# @lc code=end

# combination means you cannt select the same one one more tiem
# permutation can pick the same one
