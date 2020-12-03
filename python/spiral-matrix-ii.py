class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return [[]]
        
        res = [["A"] * n for _ in range(n)]
        self.fillNum((0,0), False, res, 1, n)
        return res
    
    def fillNum(self, pos, isDirectionUp, res, cur, n):
        row, col = pos
        
        if not (0 <= row < n and 0 <= col < n):
            return
        
        if res[row][col] != 'A':
            return
        
        res[row][col] = cur
        
        if isDirectionUp:
            self.fillNum((row - 1, col), True, res, cur + 1, n)
        
        self.fillNum((row, col + 1), False, res, cur + 1, n)
        self.fillNum((row + 1, col), False, res, cur + 1, n)
        self.fillNum((row, col - 1), False, res, cur + 1, n)
        self.fillNum((row - 1, col), True, res, cur + 1, n)
        
        
# [[01,02,03,04],
#  [16,15,14,05],
#  [11,12,13,06],
#  [10,09,08,07]]