class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # dp[i][j] ith item, j is matching the value
        
        if not A:
            return 0
        n = len(A)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        
        dp[0][0] = True
        for i in range(1, n + 1):
            dp[i][0] = True
            for j in range(1, m + 1):
                # as long as [j - A[i - 1] not out of bound
                if j >= A[i - 1]:
                    # when i am able to put A[i-1] into the sum
                    # need to check if dp[i - 1][j - A[i - 1]] can be filled
                    # with the right sum, otherwise, it can't fullfill the requirement
                    # of having exactly j, wait for the j to increase and check
                    dp[i][j] = dp[i - 1][j - A[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
            print(dp)
        
        for i in range(m, -1, -1):
            if dp[n][i] == True:
                return i
        return 0