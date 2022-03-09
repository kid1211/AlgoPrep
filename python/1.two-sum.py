class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compilment = {}

        for i in range(len(nums)):
            if nums[i] in compilment:
                return [compilment[nums[i]], i]
            compilment[target - nums[i]] = i

        return []
