public class Solution {
    // https://www.lintcode.com/problem/backpack/description
    // private int maxFit = 0;
    // private int capacity;
    // private int[] array;
    // private int total;
    
    // private void util(int index) {
    //     // System.out.println("***********Start**************");
    //     // System.out.println("index: " + index + " | total: " + total);
    //     if(total > capacity) return;
    //     maxFit = Math.max(maxFit, total);

    //     if(index == array.length) return;
        
    //     for(int i = index; i < array.length; ++i) {
    //         // System.out.println("array[i]: " + array[i]);
    //         total += array[i];
    //         util(index+1);
    //         total -= array[i];
    //         // System.out.println("***********end *" + i + "*****");
    //     }
    // }
    
    // /**
    //  * @param m: An integer m denotes the size of a backpack
    //  * @param A: Given n items with size A[i]
    //  * @return: The maximum size
    //  */
    // public int backPack(int m, int[] A) {
    //     // write your code here
    //     capacity = m;
    //     array = A;
    //     total = 0;
    //     util(0);
    //     return maxFit;
    // }
    
    
    
    
    public int backPack(int m, int[] A) {
        // write your code here
        int capacity = m;
        
        int[][] dp = new int[A.length][capacity+1];
        
        for(int j=0; j<capacity+1; ++j) {
            dp[0][j] = j >= A[0] ? A[0] : 0; 
        }
        
        for(int i=1; i< A.length;++i) {
            for(int j=0; j < capacity+1; ++j) {
                int current;
                if(A[i] <= j) {
                    int diff = j - A[i];
                    current = Math.max(A[i] + dp[i-1][diff], dp[i-1][j]);
                } else {
                    current = dp[i-1][j];
                }
                dp[i][j] = current;
            }
        }
        
        return dp[A.length-1][m];
        
    }
}