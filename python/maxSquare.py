class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """

    def maxSquare(self, matrix):
        # write your code here
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        edge = 0

        dp = [[0] * cols for _ in range(2)]
        for j in range(cols):
            # because 1 is actual the same as edge is 1
            dp[0][j] = matrix[0][j]
            edge = max(edge, dp[0][j])

        for i in range(1, rows):
            for j in range(cols):
                if j == 0:
                    dp[i % 2][j] = matrix[i][j]
                elif matrix[i][j] == 1:
                    dp[i % 2][j] = min(
                        dp[(i - 1) % 2][j], dp[i % 2][j - 1], dp[(i - 1) % 2][j - 1]) + 1
                else:
                    dp[i % 2][j] = 0
                edge = max(edge, dp[i % 2][j])
        return edge * edge
