class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # we don't know if we should take 1 or 2 at start
        # but we do know how we pick at last
        n = len(values)
        
        if n < 2:
            return True
            
        dp = [0] * 3
        suffixSum = [0] * 3 # 3 in the future
        
        dp[(n - 1) % 3] = suffixSum[(n - 1) % 3] = values[-1]
        print(dp)
        for i in range(n - 2, -1, -1):
            # dp[i + 1] has value
            sums = suffixSum[(i + 1) % 3] + values[i]
            suffixSum[i % 3] = sums
            
            # imagine 3 left, let the guy pick last one or last two
            dp[i % 3] = sums - min(dp[(i + 1) % 3], dp[(i + 2) % 3])
            print(dp)
        # sums of all the coins picked best stragey from 0 -> n
        return dp[0] > suffixSum[0] - dp[0]

class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        n = len(values)
        
        if n < 3:
            return True
        first, second = self.dfs(values, 0, {})
        return first > second
        
    def dfs(self, values, index, memo):
        if index in memo:
            return memo[index]
        
        # init
        n = len(values)
        if index == n:
            return 0, 0
        
        if index == n - 1:
            return values[index], 0
        
        if index == n - 2:
            return values[index] + values[index + 1], 0
        # first only take one
        first1, second1 = self.dfs(values, index + 1, memo)
        # first take two
        first2, second2 = self.dfs(values, index + 2, memo)
        # now become reverse
        
        total = first1 + second1 + values[index]
        first = max(second1 + values[index], second2 + values[index] + values[index + 1])
        
        memo[index] = (first, total - first)
        return memo[index]