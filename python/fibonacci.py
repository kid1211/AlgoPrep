class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):
        # write your code here
        dp = [0, 1, 0]

        for i in range(2, n + 1):
            dp[i % 3] = dp[(i - 1) % 3] + dp[(i - 2) % 3]

        return dp[(n - 1) % 3]
