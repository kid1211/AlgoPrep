class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        # write your code here
        # hashmap
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        # maps = {}
        n = len(prefix)
        for i in range(n):
            for j in range(i, n + 1):
                if prefix[j] - prefix[i] == 0:
                    return [i, j - 1]
        return []
