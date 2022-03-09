class Solution {
    var res: [[Int]] = [];
    var visited: Set<Int> = [];
    
    func permute(_ nums: [Int]) -> [[Int]] {
        helper(nums, 0, [])
        return res
    }
    
    func helper(_ nums:[Int], _ index: Int, _ curr:[Int]) {
        // var curr = curr
        if (index >= nums.count) {
            res += [curr]
            return
        }
        
        for i in 0..<nums.count {
            let val = nums[i]
            
            if visited.contains(val) {
                continue
            }
            
            visited.insert(val)
            helper(nums, index+1, curr + [val])
            visited.remove(val)
        }
    }
}