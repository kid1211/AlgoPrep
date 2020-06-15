class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    def firstWillWin(self, values):
        if not values:
            return False
        n = len(values)

        if n < 3:
            return True

        dp = [0] * 3
        suffix_sum = [0] * 3
        dp[(n - 1) % 3] = suffix_sum[(n - 1) % 3] = values[-1]

        for i in range(n - 2, -1, -1):
            rolling_sum = suffix_sum[(i + 1) % 3] + values[i]
            suffix_sum[i % 3] = rolling_sum

            dp[i % 3] = max(
                rolling_sum - dp[(i + 1) % 3],
                rolling_sum - dp[(i + 2) % 3]
            )
        return dp[0] > suffix_sum[0] - dp[0]
