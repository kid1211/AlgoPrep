class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for quick in range(len(nums)):
            if nums[quick] != 0:
                if slow != quick:
                    nums[slow] = nums[quick]
                slow += 1

        for i in range(slow, len(nums)):
            nums[i] = 0
