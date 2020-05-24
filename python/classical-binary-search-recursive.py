class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        # write your code here

        start, end = 0, len(nums) - 1

        if end < 0:
            return -1

        if end == 0:
            return end if nums[end] == target else -1

        return self.binarySearchWithRange(nums, target, start, end)

    def binarySearchWithRange(self, nums, target, start, end):
        if start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.binarySearchWithRange(nums, target, mid, end)
            else:
                return self.binarySearchWithRange(nums, target, start, mid)

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
