#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, start, end):
        # remember to have exit
        if start >= end:
            return

        left, right = start, end
        # this value should be changing
        pivot = nums[(left + right) // 2]

        # key point 2: every time you compare left & right, it should be
        # left <= right not left < right
        # to skip the pivot, cuz this thing don't need to be sorted any more
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        #              right  pivot left
        # [9, 5, 2, 9, 15,     20,   70, 40, 80, 55, 75]
        # [9, 5, 2, 9, 15]
        # [70, 40, 80, 55, 75]
        self.quicksort(nums, start, right)
        self.quicksort(nums, left, end)

        # @lc code=end
