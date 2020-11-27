class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        results = [1, 2]

        for i in range(2, n):
            results.append(results[-1] + results[-2])

        return results[-1]
