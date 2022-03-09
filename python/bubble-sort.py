#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sortedIdx = len(nums)

        while sortedIdx > 0:
            for i in range(0, sortedIdx - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            sortedIdx -= 1
        return nums

# @lc code=end


# https: // www.youtube.com/watch?v = xli_FI7CuzA
# check two items at a time
# if not sorted, swap them, if sorted skip
# when traves to the end, sorted for 1 elements,

# then repeat till the sorted index meet 0
