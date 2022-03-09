class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        # write your code here

        left, right = 0, len(nums) - 1

        if not nums:
            return -1

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


class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        # write your code here

        left, right = 0, len(nums)

        if not nums:
            return -1

        def getVal(idx):
            # this value doesn't matter as long as it can go on of the way
            return nums[idx] if idx < len(nums) else sys.maxsize

        while left <= right:
            mid = (left + right) // 2

            if getVal(mid) < target:
                left = mid + 1
            elif getVal(mid) > target:
                right = mid - 1
            else:
                return mid
        return -1

    # right is n not n - 1
    # left + 1, right - 1
