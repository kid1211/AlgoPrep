#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)

        maxN = len(nums)
        if maxN % 2 == 0:
            # print(maxN // 2)
            return (nums[maxN // 2] + nums[maxN // 2 - 1]) / 2.0
        else:
            return nums[maxN // 2]
# @lc code=end
