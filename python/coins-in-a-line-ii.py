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


class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    def firstWillWin(self, values):
        # write your code here
        if not values:
            return False

        if len(values) < 2:
            return True
        memo = {}
        first, second = self.dfs(values, 0, memo)
        print(memo)
        return first > second

    def dfs(self, values, index, memo):
        n = len(values)
        if index >= n:
            return 0, 0
        if index == n - 1:
            return values[index], 0
        if index == n - 2:
            return values[index] + values[index + 1], 0

        if index in memo:
            return memo[index]

        # so now we have more then 3 items
        first1, second1 = self.dfs(values, index + 1, memo)
        first2, second2 = self.dfs(values, index + 2, memo)
        total = first1 + second1 + values[index]

        # essentially after picking 1 or 2 coins, we will become second in the dfs above
        # because we have already picked it
        first = max(second1 + values[index], second2 +
                    values[index] + values[index + 1])

        memo[index] = (first, total - first)
        return memo[index]
