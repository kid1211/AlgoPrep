class NumArray {

    private int[] segTree;
    private int[] nums;
    
    private void buildSegmentTree(int[] nums, int[] segTree, int low, int high, int pos) {
        if(low > high) return;
        
        if (low == high) {
            segTree[pos] = nums[low];
            return;
        }
        
        int mid = low + (high - low) / 2;
        int leftChildPos = 2*pos+1;
        int rightChildPos = 2*pos+2;
        
        buildSegmentTree(nums, segTree, low, mid, leftChildPos);
        buildSegmentTree(nums, segTree, mid+1, high, rightChildPos);
        
        segTree[pos] = segTree[leftChildPos] + segTree[rightChildPos];
    }
    
    public NumArray(int[] nums) {
        int segTreeSize = 4*nums.length;
        segTree = new int[segTreeSize];
        buildSegmentTree(nums, segTree, 0, nums.length-1, 0);
        this.nums = nums;
    }
    
    private void updateSegUtil(int start, int end, int pos, int i, int diff) {     
        int mid = start + (end - start) / 2;
        
        if(i < start || i > end) {
            return;
        }
        segTree[pos] += diff;

        if(start != end) {
            updateSegUtil(start, mid, 2*pos+1, i, diff);
            updateSegUtil(mid+1, end, 2*pos+2, i, diff);
        }
    }
    
    public void update(int i, int val) {
        if(i < 0 || i >= nums.length) return;
        int difference = val - nums[i];
        nums[i] = val;
        updateSegUtil(0, nums.length-1, 0, i, difference);
    }
    
    private int sumRangeUtil(int start, int end, int pos, int i, int j) {
        if(j < start || i > end) return 0;
        if(i <= start && j >= end) return segTree[pos];
        
        int mid = start + (end - start) / 2;
        
        return sumRangeUtil(start, mid, 2*pos + 1, i, j) + sumRangeUtil(mid+1, end, 2*pos + 2, i, j);
    }
    
    public int sumRange(int i, int j) {
        if(i < 0 || j >= nums.length) return 0;
        int result = sumRangeUtil(0,nums.length-1, 0, i, j);
        return result;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */