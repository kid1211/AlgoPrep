public class Demo {

    public static int lastPosition(int[] nums, int target) {
        // write your code here
        
        int start = 0; // 0
        int end = nums.length-1; // 6
        
        while(start <= end) { // 4 <= 5
            int mid = start + (end - start) / 2; // 4
            System.out.println(mid);
            if(nums[mid] == target && (mid == end || nums[mid+1] != target)) { // 
                return mid; 
            } else if( nums[mid] < target) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        
        return -1;
    }
    public static void main(String[] args) {
        System.out.println(lastPosition(new int[]{1,2,2,2,2,4,5,5}, 2));
    }
}


