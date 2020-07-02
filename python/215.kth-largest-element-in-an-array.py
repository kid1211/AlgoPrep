class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # remember to do n - k
        return self.quickSelect(nums, 0, n - 1, n - k)

    def quickSelect(self, nums, start, end, k):
        left, right = start, end
        # needs to do this, other wise the nums is changed, the pivot no longer the same
        pivot = nums[(start + end) // 2]

        while left <= right:
            # not equal
            while left <= right and nums[left] < pivot:
                left += 1

            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # start -> right
        # left -> end
        if k <= right:
            return self.quickSelect(nums, start, right, k)
        elif left <= k:
            return self.quickSelect(nums, left, end, k)
        return pivot
