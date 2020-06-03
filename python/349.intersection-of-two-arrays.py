#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hasValue = set(nums2)

        rtn = []
        for num in nums1:
            if num not in hasValue:
                continue
            rtn.append(num)
            hasValue.remove(num)
        return rtn

# @lc code=end


[1, 2, 2, 1]\n[2, 2]
