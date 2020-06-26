class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        if m == 0 or not A:
            return 0
        # dp represent the answer if m is equal to the index
        dp = [0 for _ in range(m + 1)]
        
        for num in A:
            j = m
            # while I can add nums, check before and after I add it
            while j >= num:
                dp[j] = max(dp[j], dp[j - num] + num)
                j -= 1
        
        return dp[m]