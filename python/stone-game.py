class Solution:
    """
    @param A: An integer array
    @return: An integer
    """

    def stoneGame(self, A):
        # write your code here
        if not A:
            return 0
        n = len(A)
        rangeSum = self.getRangeSum(A, n)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i != j:
                    dp[i][j] = sys.maxsize
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] +
                                   dp[k + 1][j] + rangeSum[i][j])
        return dp[0][n - 1]

    def getRangeSum(self, A, n):
        rangeSum = [[0] * n for _ in range(n)]

        for i in range(n):
            rangeSum[i][i] = A[i]
            for j in range(i + 1, n):
                rangeSum[i][j] = rangeSum[i][j - 1] + A[j]
        return rangeSum


# - state: dp[i][j] 表示ith到jth石子合并到一起的最小花费
# - function:
#   - 预处理 sum[i][j], 表示ith到jth所有价值和
#   - dp[i][j] = min(dp[i][k] + dp[k+1][j] + sum[i][j])对于所有k处于 {i, j - 1}
# - initialize for each i dp[i][i] = 0
# - answer dp[0][n-1]
# 四边形不等式
# *****start*******
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# *****end*******
# *****start*******
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# *****end*******
# *****start*******
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 7]
# [0, 0, 0, 0]
# *****end*******
# *****start*******
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 7]
# [0, 0, 0, 0]
# *****end*******
# *****start*******
# [0, 0, 0, 0]
# [0, 0, 7, 0]
# [0, 0, 0, 7]
# [0, 0, 0, 0]
# *****end*******
# *****start*******
# [0, 0, 0, 0]
# [0, 0, 7, 17]
# [0, 0, 0, 7]
# [0, 0, 0, 0]
# *****end*******
# *****start*******
# [0, 0, 0, 0]
# [0, 0, 7, 17]
# [0, 0, 0, 7]
# [0, 0, 0, 0]
# *****end*******
# *****start*******
# [0, 5, 0, 0]
# [0, 0, 7, 17]
# [0, 0, 0, 7]
# [0, 0, 0, 0]
# *****end*******
# *****start*******
# [0, 5, 14, 0]
# [0, 0, 7, 17]
# [0, 0, 0, 7]
# [0, 0, 0, 0]
# *****end*******
# *****start*******
# [0, 5, 14, 24]
# [0, 0, 7, 17]
# [0, 0, 0, 7]
# [0, 0, 0, 0]
# *****end*******
