class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """

    def subarraySumEqualsK(self, nums, k):
        # write your code here

        # mutate to prefix sum
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        # 0 的话有一种答案 就是什么都不加
        prefixHash, ans = {0: 1}, 0

        # 算array sum的和的公式是 sums[j] - sums[i] = k
        # so sums[j] - k = sums[i] in the hash map
        for i in range(len(nums)):
            if nums[i] - k in prefixHash:
                # 在prefixhash里面有多少种组合到这个sum
                ans += prefixHash[nums[i] - k]
            # 如果没有就设置为1, 不然后+ 1
            if nums[i] not in prefixHash:
                prefixHash[nums[i]] = 1
            else:
                prefixHash[nums[i]] += 1
        return ans
