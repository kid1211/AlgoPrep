class Solution:
    """
    @param matrix: a 2D array
    @return: return a list of integers
    """
    def findDiagonalOrder(self, matrix):
        # write your code here
        result = []
        dd = collections.defaultdict(list)
        if not matrix: 
            return result
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dd[i+j].append(matrix[i][j])
        for k, v in dd.items():
            if k%2==0: dd[k].reverse()
            result += dd[k]
        return result