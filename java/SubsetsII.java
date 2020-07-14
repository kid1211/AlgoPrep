class Solution {
    // https://leetcode.com/problems/subsets-ii/submissions/
    private List<List<Integer>> result;
    private int[] nums;
    
    private void util(int startIndex, List<Integer> currentList) {
        if(startIndex > nums.length) return;

        result.add(new ArrayList<>(currentList));
        
        for(int i = startIndex; i < nums.length; ++i) {
            // We don't want to compare between two startIndexes
            // If we did that we wont have any duplicate numbers in
            // the subsets. It would become subsets with unique values.
            //
            // The solution we want for this question is non duplicate subsets,
            // the values in them can be duplicate numbers
            // Which is why we make check for i != startIndex,
            // This way we still have subsets with duplicates values in them
            // but prevent duplicate subsets.
            // Try drawing the recurrence graph for [ 1 2 2 2 ] to understand.
            if(i != startIndex && nums[i] == nums[i-1]) continue;
            currentList.add(nums[i]);
            util(i+1, currentList);
            currentList.remove(currentList.size()-1);
        }
        
    }
    
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        result = new ArrayList<>();
        if(nums == null || nums.length == 0) return result;
        Arrays.sort(nums);
        this.nums = nums;
        util(0, new ArrayList<>());
        return result;
    }
}