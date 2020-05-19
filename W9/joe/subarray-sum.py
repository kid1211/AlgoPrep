class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        # write your code here

        # [-3, 1, 2, -3, 4]
        # [-3 -2  0  -3  1]
        # 0,2 1,3
        sums = []
        cur = 0

        for num in nums:
            cur += num
            sums.append(cur)

        for lower in range(len(sums)):
            for upper in range(lower, len(sums)):
                if upper - lower == 0:
                    return [lower + 1, upper]

        return [0, 2]
