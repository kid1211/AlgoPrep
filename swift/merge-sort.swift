class Solution {
    func sortArray(_ nums: [Int]) -> [Int] {
        // merge two sorted arrry
        let length = nums.count
        if length <= 1 { return nums }
        
        let leftSorted = sortArray(Array(nums[0..<length/2]))
        let rightSorted = sortArray(Array(nums[length/2..<length]))
        var leftI = 0, rightI = 0
        let leftLength = leftSorted.count
        let rightLength = rightSorted.count
        
        var res = [Int]()
        while leftI < leftLength && rightI < rightLength {
            if leftSorted[leftI] < rightSorted[rightI] {
                res += [leftSorted[leftI]]
                leftI += 1
            } else {
                res += [rightSorted[rightI]]
                rightI += 1
            }
        }
        
        while leftI < leftLength {
            res += [leftSorted[leftI]]
            leftI += 1
        }
        
        while rightI < rightLength {
            res += [rightSorted[rightI]]
            rightI += 1
        }
        
        return res
    }
}