class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """
    def maxSubmatrix(self, matrix):
        # write your code here
        # turn it into a small problem
        if not matrix or not matrix[0]:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        maxi = -sys.maxsize + 1
        
        for lowerbound in range(n):
            # because it only depend on the last sum
            lastSums = [0 for _ in range(m)]
            for i in range(lowerbound, n):
                for j in range(m):
                    lastSums[j] += matrix[i][j]
                maxi = max(maxi, self.maxSubArray(lastSums))
        
        return maxi
        
    def maxSubArray(self, array):
        rollingSum = mini = 0
        maxi = -sys.maxsize + 1
        
        for num in array:
            rollingSum += num
            maxi = max(maxi, rollingSum - mini)
            mini = min(mini, rollingSum)
        
        return maxi
    