class Solution {
    internal var res:[[Int]] = []
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
        helper(candidates.sorted(), target, 0, 0, [])
        return res
    }
    
    func helper(_ candidates: [Int], _ target: Int, _ index: Int, _ sum: Int, _ curr: [Int]) {
        let length = candidates.count
        
        if sum == target {
            res += [curr]
            return
        }
        
        for i in index-1..<length {
            if i == -1 { continue }
            
            let item = candidates[i]
            let newSum = sum + item
            if newSum > target {
                break
            }
            
            helper(candidates, target, i + 1, newSum, curr + [item])
        }
        
    }
}