class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        if grid[0][0] == 1:
            return -1
        
        visited = set()
        theEnd = (len(grid) - 1, len(grid[0]) - 1)
        queue = collections.deque([(0, 0)])
        
        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                (x, y) = queue.popleft()
                
                if (x, y) == theEnd:
                    return steps
                
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                
                for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                    nextPoint = (x + dx, y + dy)

                    if not self.isValid(grid, nextPoint):
                        continue
                        
                    queue.append(nextPoint)
                    
        return -1
        
    def isValid(self, grid, nextPoint):
        rows = len(grid)
        cols = len(grid[0])
        x, y = nextPoint
        
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] != 1
    
    # [[0,0,1,0,0,0,0],[0,1,0,0,0,0,1],[0,0,1,0,1,0,0],[0,0,0,1,1,1,0],[1,0,0,1,1,0,0],[1,1,1,1,1,0,1],[0,0,1,0,0,0,0]]