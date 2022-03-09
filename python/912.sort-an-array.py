#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums
        
        left = self.sortArray(nums[:n//2])
        right = self.sortArray(nums[n//2:])
        
        return self.mergeSort(left, right)
    def mergeSort(self, left, right):
        i = j = 0
        maxLeft, maxRight = len(left), len(right)
        
        res = []
        while i < maxLeft and j < maxRight:
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        while i < maxLeft:
            res.append(left[i])
            i += 1
        
        while j < maxRight:
            res.append(right[j])
            j += 1
        
        return res
                
        # @lc code=end
