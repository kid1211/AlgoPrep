class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber(self, A):
        # write your code here
        if not A:
            return 0

        n = len(A)

        if n < 3:
            return max(A)

        dp = [A[0], max(A[0], A[1]), 0]

        for i in range(2, n):
            dp[i % 3] = max(dp[(i-1) % 3], dp[(i-2) % 3] + A[i])

        return dp[(n - 1) % 3]
