class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        # write your code here

        left, right = 0, len(nums) - 1

        if right < 0:
            return -1

        if right == 0:
            return right if nums[right] == target else -1

        while left + 1 < right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
