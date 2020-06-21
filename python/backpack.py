class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        # f[i][s] 前i个物品，去除一些组成s的sum

        n = len(A)
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]

        dp[0][0] = True
        for i in range(1, n + 1):
            dp[i][0] = True
            for j in range(1, m + 1):
                # speed things up
                if j >= A[i - 1]:
                    dp[i][j] = dp[i - 1][j - A[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        for j in range(m, -1, -1):
            if dp[n][j]:
                return j
        return 0
