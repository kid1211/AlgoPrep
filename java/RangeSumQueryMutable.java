class NumArray {
    // https://leetcode.com/problems/range-sum-query-mutable/submissions/
    private int[] segTree;
    private int[] nums;
    private void buildSegmentTree(int[] nums, int[] segTree, int pos, int low, int high) {
        if(low > high) return;
        
        if(low == high) {
            segTree[pos] = nums[low];
            return;
        }
        
        int mid = low + (high - low) / 2;
        
        int leftChildPos = 2 * pos + 1;
        int rightChildPos = 2 * pos + 2;
        
        buildSegmentTree(nums, segTree, leftChildPos, low, mid);
        buildSegmentTree(nums, segTree, rightChildPos, mid+1, high);
        
        segTree[pos] = segTree[leftChildPos] + segTree[rightChildPos];
    }
    
    public NumArray(int[] nums) {
        this.nums = nums;
        segTree = new int[4*nums.length];
        buildSegmentTree(nums, segTree, 0, 0, nums.length-1);
        // System.out.println(Arrays.toString(segTree));
    }
    
    private void updateUtil(int low, int high, int i, int pos, int difference) {
        if(i < low || i > high) return;
        int leftChildPos = 2 * pos + 1;
        int rightChildPos = 2 * pos + 2;
        int mid = low + (high - low) / 2;
        segTree[pos] += difference;
        
        // If we are at leaf node, no need to call further update
        if(low != high) {
            updateUtil(low, mid, i, leftChildPos, difference);
            updateUtil(mid+1, high, i, rightChildPos, difference);
        }
    }
    
    public void update(int i, int val) {
        int difference = val - nums[i];
        nums[i] = val;
        updateUtil(0, nums.length-1, i, 0, difference);
    }
    
    private int sumRangeUtil(int low, int high, int i, int j, int pos) {
        if(i > high || j < low) return 0;
        if(i <= low && j >= high) return segTree[pos];
        
        int mid = low + (high - low) / 2;
        
        return sumRangeUtil(low, mid, i, j, 2*pos+1) + sumRangeUtil(mid+1, high, i, j, 2*pos+2);
        
    }
    
    public int sumRange(int i, int j) {
        return sumRangeUtil(0, nums.length-1, i, j, 0);
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */