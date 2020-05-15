#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash table
        soulMateDict = {}

        for i in range(len(nums)):
            if nums[i] in soulMateDict:
                return sorted([soulMateDict[nums[i]], i])

            soulMateDict[target - nums[i]] = i
        return [1, 2]
# @lc code=end
