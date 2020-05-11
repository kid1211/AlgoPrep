#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth = 0
        # mustBeSmaller = 0
        largest = 0

        for idx in range(len(nums)):
            if nums[idx] > largest:
                largest = nums[idx]

        # then you have the largest
        # find the second largest
# @lc code=end
