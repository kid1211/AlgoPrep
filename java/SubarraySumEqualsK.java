class Solution {
    // https://leetcode.com/problems/subarray-sum-equals-k/
    HashMap<Integer, Integer> map = new HashMap<>();
    public int subarraySum(int[] nums, int k) {
        int sum = 0;
        int count = 0;
        map.put(0, 1);
        for(int i = 0; i < nums.length; ++i) {
            sum += nums[i];
            if(map.containsKey(sum - k)) {
                count += map.get(sum - k);
            }
            // The following increment to map should come after incrementing the count
            // otherwise the count would end up also including the current value if K = 0;
            map.put(sum, map.getOrDefault(sum, 0) + 1);

        }
        return count;
    }
}