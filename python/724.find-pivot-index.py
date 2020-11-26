class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return -1

        total = sum(nums)
        rolling = 0

        for i in range(n):
            if rolling == total - rolling - nums[i]:
                return i

            rolling += nums[i]

        return -1
