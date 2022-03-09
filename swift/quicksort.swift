class Solution {
    func sortArray(_ nums: [Int]) -> [Int] {
        var nums = nums
        // print(5/1, 5/2, 5/3, 5/4, 5/5)
        quickSort(&nums, 0 , nums.count - 1)
        return nums
    }
    
    func quickSort(_ nums: inout [Int], _ start: Int, _ end: Int) {
        if start >= end {
            return
        }
        
        var l = start, r = end;
        
        let pivot = nums[((start + end) / 2)]
        
        while l <= r {
            while l <= r && nums[l] < pivot { l += 1 }
            while l <= r && nums[r] > pivot { r -= 1 }
            
            if l <= r {
                nums.swapAt(l, r)
                l += 1
                r -= 1
            }
        }
                     
        
        quickSort(&nums, start, r)
        quickSort(&nums, l, end)
    }
}