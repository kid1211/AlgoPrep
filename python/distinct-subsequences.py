class Solution:
    """
    @param S: A string
    @param T: A string
    @return: Count the number of distinct subsequences
    """

    def numDistinct(self, S, T):
        # write your code here
        n, m = len(S), len(T)
        if n < m:
            return 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if S[i - 1] != T[j - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        return dp[n][m]
