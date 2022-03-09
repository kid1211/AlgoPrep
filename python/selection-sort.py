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


# https: // www.youtube.com/watch?v = g-PGLbMth_g
# sort from left to right, take notes on the index of the smallest one
# start from the smallest one, then have two pointers,
# pointer 1 always poitn to the smallest one while pointer 2 traves and find the smaller open
# once found, move the pointer 1 to that open
# when done, swap smallest one with the sorted index
