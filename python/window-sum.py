class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        if len(nums) < k or k == 0:
            return []

        upperBound = k
        currentSum = sum(nums[i] for i in range(k))
        results = [currentSum]

        while upperBound < len(nums):
            currentSum += nums[upperBound]
            currentSum -= nums[upperBound - k]
            results.append(currentSum)
            upperBound += 1

        return results
