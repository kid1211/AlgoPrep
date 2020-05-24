class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        # write your code here
        length = len(nums)

        if length == 0:
            return 0

        if length == 1:
            return 1 if nums[0] < k else 0

        # we need to mutate the array
        left = 0
        while left < length and nums[left] < k:
            left += 1

        if left == length or left == length - 1:
            return left
        # make sure they dont' go over bound
        right = left + 1

        while right < length:
            if nums[right] >= k:
                right += 1
            else:
                # swap
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
        return left
