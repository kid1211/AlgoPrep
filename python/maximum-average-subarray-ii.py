class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """

    def maxAverage(self, nums, k):
        # write your code here
        if not nums:
            return 0

        left, right = min(nums), max(nums)

        while right - left > 1e-5:
            mid = (left + right) / 2.0

            if self.checkSubArray(nums, k, mid):
                left = mid
            else:
                right = mid
        # find smaller one
        return left

    def checkSubArray(self, nums, k, average):
        # sums of all the value - average
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num - average)

        min_prefix_sum = 0
        # same logic as maximum sub array
        for i in range(k, len(nums) + 1):
            if prefix_sum[i] - min_prefix_sum >= 0:
                return True
            min_prefix_sum = min(min_prefix_sum, prefix_sum[i - k + 1])

        return False
