#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        visited = set()
        self.dfs([], visited, results, nums)
        return results

    def dfs(self, current, visited, results, nums):
        length = len(nums)
        if len(current) == length:
            results.append(list(current))
            return

        for i in range(length):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            current.append(nums[i])
            self.dfs(current, visited, results, nums)
            current.pop()
            visited.remove(nums[i])

# @lc code=end
