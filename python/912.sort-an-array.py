#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)

    def mergesort(self, nums):
        length = len(nums)

        if length <= 1:
            return nums

        leftSorted = self.mergesort(nums[:length // 2])
        rightSorted = self.mergesort(nums[length // 2:])

        left, right = 0, 0
        maxLeft, maxRight = len(leftSorted), len(rightSorted)
        rtn = []

        while left < maxLeft and right < maxRight:
            if leftSorted[left] <= rightSorted[right]:
                rtn.append(leftSorted[left])
                left += 1
            else:
                rtn.append(rightSorted[right])
                right += 1

        while left < maxLeft:
            rtn.append(leftSorted[left])
            left += 1
        while right < maxRight:
            rtn.append(rightSorted[right])
            right += 1

        return rtn
        # @lc code=end
