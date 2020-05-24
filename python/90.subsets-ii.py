#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.helper([], 0, results, sorted(nums))
        return results

    def helper(self, current, idx, results, nums):
        # if len(current) > 0 and nums[idx] == current[-1]:
        print(current)
        results.append(list(current))

        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            #     results.pop()
            current.append(nums[i])
            self.helper(current, i + 1, results, nums)
            current.pop()

# @lc code=end
