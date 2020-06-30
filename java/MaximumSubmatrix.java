public class Solution {
    // https://www.lintcode.com/problem/maximum-submatrix/description
    private int maxSum;
    private int[] rowPrefixSum;
    private int m;
    private int n;
    
    private void computePrefixSum(int colIndex, int[][] matrix) {
        for(int i=0; i < m; ++i) {
            rowPrefixSum[i] += matrix[i][colIndex];
        }
    }
    
    private void maxSubarray() {
        int currentSum = 0;
        for(int i = 0; i < m; ++i) {
            currentSum = Math.max(currentSum + rowPrefixSum[i], rowPrefixSum[i]);
            maxSum = Math.max(currentSum, maxSum);
        }
    }
    
    /**
     * @param matrix: the given matrix
     * @return: the largest possible sum
     */
    public int maxSubmatrix(int[][] matrix) {
        // write your code here
        m = matrix.length;
        if(m == 0) return 0;
        n = matrix[0].length;
        if(n == 0) return 0;
        
        rowPrefixSum = new int[m];
        
        for(int leftColIndex = 0; leftColIndex < n; ++leftColIndex) {
            for(int rightColIndex = leftColIndex; rightColIndex < n; ++rightColIndex) {
                computePrefixSum(rightColIndex, matrix);
                maxSubarray();
            }
            rowPrefixSum = new int[m];
        }
        
        return maxSum;
    }
}