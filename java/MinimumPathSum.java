public class MinimumPathSum {
    
}public class Solution {
    // https://www.lintcode.com/problem/minimum-path-sum/description
    /**
     * @param grid: a list of lists of integers
     * @return: An integer, minimizes the sum of all numbers along its path
     */
    public int minPathSum(int[][] grid) {
        // write your code here
        
        int m = grid.length;
        if(m == 0) return 0;
        int n = grid[0].length;
        if(n == 0) return 0;
        
        int[][] dp = new int[m][n];
        int count = 0;
        for(int i=0; i < n; ++i) {
            count += grid[0][i];
            dp[0][i] = count;
        }
        
        count = 0;
        for(int i=0; i < m; ++i) {
            count += grid[i][0];
            dp[i][0] = count;
        }
        
        for(int i = 1; i < m; ++i) {
            for(int j = 1; j < n; ++j) {
                dp[i][j] = grid[i][j] + Math.min(dp[i-1][j], dp[i][j-1]);     
            }
        }
        
        return dp[m-1][n-1];
    }
}