class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
            
        n, m = len(grid), len(grid[0])
        dp = [[0] *  m for _ in range(n)]
        
        rolling = 0
        for i in range(n):
            rolling += grid[i][0]
            dp[i][0] = rolling
        
        rolling = 0
        for i in range(m):
            rolling += grid[0][i]
            dp[0][i] = rolling

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
            # print(dp)
        return dp[n - 1][m - 1]