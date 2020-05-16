class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZeroes(self, nums):
        # write your code here

        length = len(nums)

        if length <= 1:
            return nums

        # [0 1 0 3 12]
        # [1 1 0 3 12]
        # [1 3 0 3 12]
        # left is indecated teh sorted ones
        left, right = 0, 0

        while right < length:
            while right < length and nums[right] == 0:
                right += 1

            if right < length:
                nums[left] = nums[right]
                left += 1
                right += 1

        for i in range(left, length):
            nums[i] = 0
        return nums
