class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """

    def minimumSize(self, nums, s):
        # write your code here
        n = len(nums)
        j, sums = 0, 0
        shortest = sys.maxsize

        for i in range(n):
            while j < n and sums < s:
                sums += nums[j]
                j += 1

            if sums >= s:
                shortest = min(shortest, j - i)

            sums -= nums[i]

        return shortest if shortest != sys.maxsize else -1
