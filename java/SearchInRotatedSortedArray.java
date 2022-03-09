public class SearchInRotatedSortedArray {
    // Lintcode: https://www.lintcode.com/problem/search-in-rotated-sorted-array/description
    // Leetcode: https://leetcode.com/problems/search-in-rotated-sorted-array/
    public int search(int[] A, int target) {      
        if (A.length == 0) return -1;
        
        int start = 0;
        int end = A.length - 1;
        
        while(start < end) {
            int mid = start + (end - start) / 2;
            
            if (mid !=0 && A[mid] < A[mid-1]) {
                start = mid;
                break;
            } else if (A[mid] > A[end]) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        
        if(target >= A[start] && target <= A[A.length-1]) {
            end = A.length-1;
        } else {
            end = start;
            start = 0;
        }
        
        while(start <= end) {
            int mid = start + (end - start) / 2;
            if(A[mid] == target) {
                return mid;
            }else if(target < A[mid]) {
                end = mid-1;
            } else {
                start = mid+1;
            }
        }
        
        return -1;
    }
}