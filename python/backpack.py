class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [0 for _ in range(m + 1)]

        for num in A:
            # fill the dp in backward
            j = m
            # means i have enough space to take num
            while j >= num:
                dp[j] = max(dp[j], dp[j - num] + num)
                j -= 1

        return dp[m]
