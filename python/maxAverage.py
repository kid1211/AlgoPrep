class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """

    def maxAverage(self, nums, k):
        sums = []
        length = len(nums)

        curr = 0
        for num in nums:
            curr += num
            sums.append(curr)
        # print(sums)

        rtn = -sys.maxsize + 1
        for i in range(length):
            for j in range(i + k - 1, length):
                left = 0 if i == 0 else sums[i - 1]
                right = sums[j]

                avg = (right - left) / (j - i + 1)
                rtn = max(avg, rtn)

        return rtn
