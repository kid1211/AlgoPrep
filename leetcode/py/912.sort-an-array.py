#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sortedIdx = 0
        length = len(nums)

        while sortedIdx < length:
            i, j = sortedIdx, sortedIdx

            while j < length:
                if nums[j] < nums[i]:
                    i = j
                j += 1

            nums[sortedIdx], nums[i] = nums[i], nums[sortedIdx]
            sortedIdx += 1
        return nums
# @lc code=end
