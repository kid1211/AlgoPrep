class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # dp represent the matches of the [0 -> i] from A and [0 -> j] from B
        n, m = len(A), len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # do the common one first, assume the current
                # character is not matching
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
        return dp[n][m]


# - state: f[i][j] 代表了第一个sequence 的前i个数字/字符, 配上第二个sequnce的前j个
# - function: f[i][j] = 研究第i个和第j个的匹配关系（上， 左，左上， 三个状态)
# - initialization : f[i][0] 和 f[0][j]
# - answer f[n][m] min/max/数目/存在关系
#   - n + 1 或 m + 1， 记得考虑空字符串
# - n = s1.length()
# - m = s2.length()
# - 阶梯技巧花矩阵,填写矩阵

# aaaaa
# aaabaa