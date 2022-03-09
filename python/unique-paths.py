class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # write your code here
        dp = [0] * n
        dp[0] = 1

        for _ in range(m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[n - 1]
