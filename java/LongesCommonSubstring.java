public class Solution {
    // https://www.lintcode.com/problem/longest-common-substring/description
    /**
     * @param A: A string
     * @param B: A string
     * @return: the length of the longest common substring.
     */
    public int longestCommonSubstring(String A, String B) {
        // write your code here
        
        int n = A.length();
        int m = B.length();
        
        if(n == 0 || m == 0) return 0;
        int[][] dp = new int[n+1][m+1];
    
        int max = 0;
        for(int i = 0; i <= n; ++i) {
            for(int j = 0; j <= m; ++j) {
                int value = 0;
                if(i == 0 || j == 0) {
                    continue;
                }
                if(A.charAt(i-1) == B.charAt(j-1)) {
                    value = dp[i-1][j-1] + 1;
                    max = Math.max(max, value);
                    dp[i][j] = value;
                }
            }
        }
        return max;
    }
}