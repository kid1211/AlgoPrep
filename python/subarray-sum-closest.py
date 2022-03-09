class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySumClosest(self, nums):
        # write your code here
        n = len(nums)
        prefix = [(0, -1)]

        for i in range(n):
            prefix.append((prefix[-1][0] + nums[i], i))

        prefix.sort()
        closest, res = sys.maxsize, []
        for i in range(1, n + 1):
            if closest > prefix[i][0] - prefix[i - 1][0]:
                closest = prefix[i][0] - prefix[i - 1][0]
                idxs = [prefix[i][1], prefix[i - 1][1]]
                left = min(idxs) + 1
                right = max(idxs)
                res = [left, right]
        return res

# sort the prefix sum,
# check the one next to each other, their delta is the smallest
# if found then set res
