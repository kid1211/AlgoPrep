class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """

    def binarySearch(self, nums, target):
        # write your code here

        left, right = 0, len(nums) - 1

        if right < 0:
            return -1

        if right == 0:
            return right if nums[right] == target else -1

        while left + 1 < right:

            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid
            elif nums[mid] < target:
                left = mid

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1


class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """

    def binarySearch(self, nums, target):
        # write your code here
        left, right = 0, len(nums)

        if not nums:
            return -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        print(left, right)
        # if you want to find the first then use left
        # if you want to find th elast then use right
        # because of the above logic, your >=, and <= need to change accordingly

        # in this case, because you wang the first matching, so if it was equal
        # drop the right one, because we want the first one

        return left if nums[left] == target else -1


# left and right overlap
# -1 and + 1
# len start from end
