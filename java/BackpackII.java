public class Solution {
    // https://www.lintcode.com/problem/backpack-ii/description
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @param V: Given n items with value V[i]
     * @return: The maximum value
     */
    public int backPackII(int m, int[] A, int V[]) {
        // write your code here
        int[][] dp = new int[A.length][m + 1];
        
        for(int j=0; j<=m; ++j) {
            dp[0][j] = j >= A[0] ? V[0] : 0; 
        }

        for (int i = 1; i < A.length; i++) {
            for (int j = 0; j <= m; j++) {
                if (j < A[i]) {
                    dp[i][j] = dp[(i - 1)][j];
                } else {
                    int diff = j - A[i];
                    dp[i][j] = Math.max(dp[(i - 1)][j], V[i] + dp[i-1][diff]);
                }
            }
        }
        return dp[A.length-1][m];
    }
}