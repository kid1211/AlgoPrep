class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        # write your code here
        n, m = len(A), len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # to avoid do final for loop again
        ans = 0
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    # if the one prev was not the same start from 0
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
        
        return ans