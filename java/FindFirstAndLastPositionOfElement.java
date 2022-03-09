class Solution {
    // https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
    // https://www.youtube.com/watch?v=dVXy6hmE_0U&t=328s
    private int firstPosition(int[] nums, int target) {
        int firstPosition = -1;
        int start = 0;
        int end = nums.length - 1;
        
        while(start <= end) {
            int mid = start + (end - start) / 2;
            
            if(target <= nums[mid]){
                firstPosition = mid;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return firstPosition;
    }

    public int[] searchRange(int[] nums, int target) {        
        int firstPosition = firstPosition(nums, target);
        int lastPosition = firstPosition(nums, target+1) - 1;
        
        if(firstPosition == -1 || nums[firstPosition] != target) return new int[]{-1, -1};
        if(lastPosition < 0) return new int[]{firstPosition, nums.length - 1};
        return new int[]{firstPosition, lastPosition};

    }
}