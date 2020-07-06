class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            # odd [1, 2, 3, 4, 5] 5 // 2 = 2
            return self.findKthLargest(nums1, 0, nums2, 0, n // 2 + 1)
        else:
            # even [1, 2, 3, 4, 5, 6] 6 // 2 = 3
            lower = self.findKthLargest(nums1, 0, nums2, 0, n // 2 + 1)
            upper = self.findKthLargest(nums1, 0, nums2, 0, n // 2)
            return (lower + upper) / 2

    def findKthLargest(self, nums1, idx1, nums2, idx2, k):
        if len(nums1) == idx1:
            return nums2[idx2 + k - 1]  # k largest not smallest
        if len(nums2) == idx2:
            return nums1[idx1 + k - 1]
        if k == 1:
            return min(nums1[idx1], nums2[idx2])

        # Try get median
        # [1, 2, 3, 4, 5] find 3 - > find (3 // 2 - 1) =>
        a = self.getValue(nums1, idx1 + k // 2 - 1)
        b = self.getValue(nums2, idx2 + k // 2 - 1)

        if b is None or (a and a < b):
            return self.findKthLargest(nums1, idx1 + k // 2, nums2, idx2, k - k // 2)
        return self.findKthLargest(nums1, idx1, nums2, idx2 + k // 2, k - k // 2)

        # see if the median is in range
    def getValue(self, arr, idx):
        return arr[idx] if idx < len(arr) else None


// TODO: turn to kth smallest
