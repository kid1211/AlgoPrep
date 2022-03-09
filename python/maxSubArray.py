class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        # write your code here
        mini, maxi = 0, -sys.maxsize
        prefixSum = 0

        for num in nums:
            prefixSum += num
            # only going to remove minimum that start from zero, can't start the start
            maxi = max(maxi, prefixSum - mini)
            mini = min(mini, prefixSum)

        return maxi
