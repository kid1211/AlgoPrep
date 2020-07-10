public class Solution {
    // https://www.lintcode.com/problem/first-position-of-target/description
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    public int binarySearch(int[] nums, int target) {
        // write your code here
        
        int start = 0;
        int end = nums.length - 1;
        while( start <= end) {
            int mid = start + (end - start) / 2;
            if(nums[mid] == target) {
                end = mid;
            };
            
            if( nums[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        // System.out.println("start: " + start + " | end: " + end);
        return nums[start] == target ? start : -1 ;
    }
}