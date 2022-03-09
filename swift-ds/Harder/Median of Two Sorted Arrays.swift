// merge two sorted array and find kth is the easiest
class Solution {
    func findMedianSortedArrays(_ nums1: [Int], _ nums2: [Int]) -> Double {
        [0, 1, 2, 3, 4, 5]
        func findKth(_ id1: Int, _ id2: Int, _ k: Int) -> Int {
            guard id1 < nums1.count else { return nums2[id2 + k - 1] }
            guard id2 < nums2.count else { return nums1[id1 + k - 1] }
            guard k > 1 else { return min(nums1[id1], nums2[id2]) }
            
            let halfKth1 = id1 + k / 2 - 1 < nums1.count ? nums1[id1 + k / 2 - 1] : Int.max
            let halfKth2 = id2 + k / 2 - 1 < nums2.count ? nums2[id2 + k / 2 - 1] : Int.max
            
            if halfKth1 < halfKth2 {
                return findKth(id1 + k / 2, id2, k - k / 2)
            } else {
                return findKth(id1, id2 + k / 2, k - k / 2)
            }
        }
        
        let n = nums1.count + nums2.count
        if n % 2 == 0 {
            return (
                Double(findKth(0, 0, n / 2)) +
                Double(findKth(0, 0, n / 2 + 1))
            ) / 2.0
        } else {
            return Double(findKth(0, 0, n / 2 + 1))
        }
    }
}