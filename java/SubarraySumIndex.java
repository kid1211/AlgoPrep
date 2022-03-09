public class Solution {
    // https://www.lintcode.com/problem/subarray-sum/description
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number and the index of the last number
     */
    public List<Integer> subarraySum(int[] nums) {
        // write your code here

        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
        int sum = 0;
        for(int i=0; i < nums.length; ++i) {
            sum += nums[i];
            if (map.containsKey(sum)) return Arrays.asList((map.get(sum) + 1), i);
            map.put(sum, i);
        }
        
        return new ArrayList<Integer>();
    }
}