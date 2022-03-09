class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # compare to empty string
        for i in range(m + 1):
            dp[0][i] = i
        for i in range(n + 1):
            dp[i][0] = i
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    # dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                    dp[i][j] = dp[i - 1][j - 1] # no additional effort
                else:
                    # from word1 prespective: replace one| insert a new one | remove a new one
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[n][m]