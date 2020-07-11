class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        # write your code here
        prefix = []
        rolling = 0
        n = len(nums)

        for i in range(n):
            rolling += nums[i]
            prefix.append(rolling)

        for lower in range(n):
            for higher in range(lower, n):
                if prefix[higher] - prefix[lower] == 0:
                    return [lower + 1, higher]

        return []
