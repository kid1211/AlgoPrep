#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if len(nums) == 1:
            return nums[0]

        return self.findKthLargestWithinRange(nums, len(nums) - k, 0, len(nums) - 1)

    def findKthLargestWithinRange(self, nums, k, start, end):

        left, right = start, end
        pivot = nums[(start + end) // 2]

        while left <= right:
            # print(nums)
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if k <= right:
            return self.findKthLargestWithinRange(nums, k, start, right)
        elif left <= k:
            return self.findKthLargestWithinRange(nums, k, left, end)

        return pivot

# @lc code=end
