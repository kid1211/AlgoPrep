public class Solution {
    // https://www.lintcode.com/problem/stone-game/description
    private int[] getPrefixSum(int[] A) {
        int[] prefixSum = new int[A.length + 1];
        int sum = 0;
        prefixSum[0] = 0;
        for(int i = 0; i < A.length; ++i) {
            sum += A[i];
            prefixSum[i+1] = sum; 
        }
        return prefixSum;
    }
    /**
     * @param A: An integer array
     * @return: An integer
     */
    public int stoneGame(int[] A) {
        // write your code here
        if(A.length == 0) return 0;
        int[] prefixSum = getPrefixSum(A);
        int n = A.length;
        
        int[][] dp = new int[n][n];
        
        // for(int i=0; i<A.length; ++i) {
        //     dp[i][i] = 0;
        // }
        //   0 1 2 3
        // [ 4 1 1 4]
        // dp[i][j] = 1 2 
        
        //     0   1   2   3
        // 0   0   5      
        // 1   -   0   2   8
        // 2   -   -   0   5
        // 3   -   -   -   0
        
        // This for loop fills the dp 2d array diagonally
        // for(int interval=1; interval < n; ++interval) {
        //     for(int row = 0; row < n - interval; ++ row) {
        //         int col = row + interval;
        //         int sum = prefixSum[col+1] - prefixSum[row];
        //         int minScore = Integer.MAX_VALUE;
        //         for(int i=row; i<col; ++i) {
        //             minScore = Math.min(minScore, dp[row][i] + dp[i+1][col] + sum);
        //         }
        //         dp[row][col] = minScore;
        //     }
        // }
        
        
        // This for loop fils the dp 2d array from bottom row working it's way up one row at a time        
        for(int row=n-2; row >= 0; --row) {
            for(int col = row+1; col < n; ++col) {
                int sum = prefixSum[col+1] - prefixSum[row];
                int minScore = Integer.MAX_VALUE;
                for(int i=row; i<col; ++i) {
                    minScore = Math.min(minScore, dp[row][i] + dp[i+1][col] + sum);
                }
                dp[row][col] = minScore;
            }
        }
        
        return dp[0][A.length-1];
    }
}