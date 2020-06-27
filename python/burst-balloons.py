class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def maxCoins(self, nums):
        # write your code here
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def getValue(idx):
            return nums[idx] if 0 <= idx < n else 1

        def getDP(start, end):
            def isValid(idx):
                return 0 <= idx < n

            if start <= end and isValid(start) and isValid(end):
                return dp[start][end]
            else:
                return 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # decided which ballon to pop
                left, right = getValue(i - 1), getValue(j + 1)
                # no need to set -sys.maxsize, because the value are all positive
                for k in range(i, j + 1):
                    popBallon = getDP(i, k - 1) + getDP(
                        k + 1, j) + left * right * nums[k]
                    dp[i][j] = max(dp[i][j], popBallon)

        return getDP(0, n - 1)