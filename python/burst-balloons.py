class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """

    def maxCoins(self, nums):
        if not nums:
            return 0

        nums = [1, *nums, 1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                for k in range(i + 1, j):
                    score = nums[i] * nums[j] * nums[k]
                    dp[i][j] = max(dp[i][k] + dp[k][j] + score, dp[i][j])

        return dp[0][n - 1]
