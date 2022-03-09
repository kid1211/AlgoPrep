class Solution {
    // Linear scan for finding the median O(m+n)
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        int nums1Index = 0;
        int nums2Index = 0;
        
        double previousValue = 0;
        double currentValue = 0;
        
        double medianIndex = (nums1.length + nums2.length) / 2 + 1;
        
        for(int i = 0; i < medianIndex; ++i) {
            previousValue = currentValue;
            
            if(nums2Index >= nums2.length || nums1Index < nums1.length && nums1[nums1Index] <= nums2[nums2Index]) {
                currentValue = nums1[nums1Index];
                nums1Index++;
            } else {
                currentValue = nums2[nums2Index];
                nums2Index++;
            }
        }
        
        return (nums1.length + nums2.length) % 2 == 0 ? (previousValue + currentValue) / 2 : currentValue;
    }
}