#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # length = len(numbers)
        # if length == 0:
        #     # this won't actually happen
        #     return [-1, -1]

        left, right = 0, len(numbers) - 1

        # can remove this because left and right is in range for sure

        def sum(left, right):
            return (numbers[left] + numbers[right])

        while left < right and sum(left, right) != target:
            if sum(left, right) > target:
                right -= 1
            if sum(left, right) < target:
                left += 1

        return [left + 1, right + 1]

# @lc code=end
