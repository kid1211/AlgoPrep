class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """

    def firstWillWin(self, n):
        # dp represent if the start will be winning at n coin
        dp = [False, True, True]

        for i in range(n + 1):
            dp[i % 3] = not dp[(i - 1) % 3] or not dp[(i - 2) % 3]

        return dp[n % 3]
