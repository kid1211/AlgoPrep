class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        self.rows = len(matrix)
        if self.rows == 0:
            return False
        self.cols = len(matrix[0])
        self.target = target
        self.matrix = matrix

        left, right = 0, self.rows * self.cols - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if self.compareWithTarget(mid) == 0:
                return True
            elif self.compareWithTarget(mid) < 0:
                # target in left side
                # mide - target should be greater
                right = mid
            else:
                left = mid

        return self.compareWithTarget(left) == 0 or self.compareWithTarget(right) == 0

    def compareWithTarget(self, idxOneD):
        x = idxOneD // self.cols
        y = idxOneD % self.cols
        # print(idxOneD, x, y)
        return self.target - self.matrix[x][y]

        # x, y =
    # midX, midY = self.getCoordinate(midIdx)
        # mid = matrix[midX][midY]


# [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
# 7
