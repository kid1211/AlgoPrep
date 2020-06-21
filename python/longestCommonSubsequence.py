class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """

    def longestCommonSubsequence(self, A, B):
        # write your code here
        if not A or not B:
            return 0
        n, m = len(A), len(B)
        # include empty string
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                # why -1
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = max(dp[i + 1][j],
                                           dp[i][j + 1], dp[i][j] + 1)
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[n][m]
