class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def lastPosition(self, nums, target):
        # write your code here

        left, right = 0, len(nums) - 1

        if right < 0:
            return -1

        if left == right:
            return left if nums[left] == target else -1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid
            elif nums[mid] > target:
                right = mid

        if nums[right] == target:
            return right
        elif nums[left] == target:
            return left
        else:
            return -1
