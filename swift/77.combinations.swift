class Solution {
    var res: [[Int]] = []
    
    func combine(_ n: Int, _ k: Int) -> [[Int]] {
        helper(Array(1...n), 0, [], k)
        return res
    }
    
    func helper(_ nums:[Int], _ index: Int, _ curr: [Int], _ k: Int) {
        if (curr.count >= k) {
            res += [curr]
            return
        }
        
        for i in index..<nums.count {
            helper(nums, i + 1, curr + [nums[i]], k)
        }
    }
}