#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1

        if end < 0:
            return -1
        if end == 0:
            return nums[0]

        return self.findMinWithinRange(nums, start, end)

    def findMinWithinRange(self, nums, start, end):
        # print(nums[start: end + 1])
        if start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[end]:
                return self.findMinWithinRange(nums, mid, end)
            else:
                return self.findMinWithinRange(nums, start, mid)

        startVal, endVal = nums[start], nums[end]
        return startVal if startVal < endVal else endVal
# @lc code=end


# [4, 5, 6, 7, 8, 9, 10, 0, 1, 2]
# mid = 8

# if mid > mid - 1:
#     left = mid

# [8, 9, 10, 0, 1, 2]
# mid = 10

# if mid > mid - 1:
#     left = mid

# [10, 0, 1, 2]
# mid = 0

# # x if mid > mid - 1:
# # right = mid

# [10, 0]

# [1, 2, 3]
# mid = 2

# mid > mid - 1 and mid < end
