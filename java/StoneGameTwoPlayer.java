class Solution {
    // https://leetcode.com/problems/stone-game/
    public boolean stoneGame(int[] piles) {
        int n = piles.length; 
        int[][] dp = new int[n][n];
        
        for(int i = 0; i < piles.length; ++i) {
           dp[i][i] = piles[i];
        }
        // System.out.println(Arrays.toString(dp[1]));
        
        for(int interval = 1; interval < n; ++interval) {
            for(int row = 0; row < n - interval; ++row) {
                
                int col = row + interval;
                
                int pickLeft = piles[row] - dp[row+1][col];
                int pickRight = piles[col] - dp[row][col-1];
                
                dp[row][col] = Math.max(pickLeft, pickRight);
            }
        }
        
        return dp[0][n-1] > 0;
    }
}