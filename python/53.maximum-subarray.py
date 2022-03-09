#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 0:
            return - 1
        if length == 1:
            return nums[0]
        rollingSum = nums[0]
        temp = [rollingSum]
        for i in range(1, length):
            rollingSum += nums[i]
            temp += [rollingSum]

        maximum = -sys.maxsize + 1
        for i in range(length):
            for j in range(i + 1, length):
                curr = temp[j] - temp[i]
                maximum = curr if maximum < curr else maximum
        return maximum
        # rollingSum[]
# @lc code=end
