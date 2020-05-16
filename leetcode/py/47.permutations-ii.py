#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        visited = set()
        self.dfs([], visited, results, sorted(nums))
        return results

    def dfs(self, current, visited, results, nums):
        print(current)
        length = len(nums)
        currentLength = len(current)
        if length == currentLength and currentLength > 0:
            results.append(list(current))
            return

        for i in range(length):
            if i in visited:
                continue
            if i > 0 and nums[i] == nums[i-1] and not i - 1 in visited:
                continue

            visited.add(i)
            current.append(nums[i])
            self.dfs(current, visited, results, nums)
            current.pop()
            visited.discard(i)

# @lc code=end
