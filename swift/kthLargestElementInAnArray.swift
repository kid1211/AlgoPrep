class Solution {
    func findKthLargest(_ nums: [Int], _ k: Int) -> Int {
        var nums = nums
        let length = nums.count
        return helper(&nums, 0, length - 1, length - k)
    }
    
    func helper(_ nums: inout [Int], _ start: Int, _ end: Int, _ k: Int) -> Int {
        var l = start, r = end
        let pivot = nums[(start + end) / 2]
        
        while l <= r {
            while l <= r && nums[l] < pivot { l += 1 }
            while l <= r && nums[r] > pivot { r -= 1 }
            
            if l <= r {
                nums.swapAt(l, r)
                l += 1
                r -= 1
            }
        }
        if k <= r {
            return helper(&nums, start, r, k)
        } else if k >= l {
            return helper(&nums, l, end, k)
        } else {
            // print(nums)
            return pivot
        }
    }
}