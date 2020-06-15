class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber2(self, nums):
        # write your code here
        if not nums:
            return 0

        n = len(nums)

        if n < 4:
            return max(nums)

        lDP = [nums[0], max(nums[0], nums[1], 0), 0]
        rDP = [0, nums[1], max(nums[1], nums[2])]

        def accumulate(dp):
            dp[i % 3] = max(dp[(i - 1) % 3], dp[(i - 2) % 3] + nums[i])

        for i in range(2, n):
            if i != n - 1:
                accumulate(lDP)
            if i != 2:
                accumulate(rDP)

        return max(lDP[(n - 2) % 3], rDP[(n - 1) % 3])
