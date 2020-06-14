class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """

    def maxSubmatrix(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        maxSum = -sys.maxsize + 1
        rows, cols = len(matrix), len(matrix[0])

        for topRow in range(rows):
            lastSumsArray = [0 for _ in range(cols)]
            for row in range(topRow, rows):
                mini, prefixSum = 0, 0
                for col in range(cols):
                    lastSumsArray[col] += matrix[row][col]
                    prefixSum += lastSumsArray[col]
                    maxSum = max(maxSum, prefixSum - mini)
                    mini = min(mini, prefixSum)
        return maxSum

# [[2,-57],[49,-52]]

# [[23,90,-39,-100,89,-10],[-7,14,-36,78,14,-57],[-80,63,-34,7,-17,-23],[-48,-70,47,-29,-79,5],[-10,-12,-59,64,97,-8],[92,35,28,-86,-21,-9]]
# [[-44,-98,3,93,26,26],[63,-92,55,-20,-30,17],[88,87,65,-70,-43,54],[-74,92,-19,-45,25,-61],[-30,20,-97,-99,-60,-69],[-47,20,-54,-10,-21,-52]]

# [23,90,-39,-100,89,-10
# [-7,14,-36,78,14,-57
# [-80,63,-34,7,-17,-23]
# [-48,-70,47,-29,-79,5]
# [-10,-12,-59,64,97,-8]
# [92,35,28,-86,-21,-9]

# [23, 113, 74, -26, 63, 53]
# [16, 120, 45, 23, 126, 59]
# [-64, 103, -6, -21, 65, -25]
# [-112, -15, -77, -121, -114, -199]
# [-122, -37, -158, -138, -34, -127]
# [-30, 90, -3, -69, 14, -88]
