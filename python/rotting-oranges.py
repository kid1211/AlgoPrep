from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        queue = deque()
        goodBoi = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    goodBoi += 1

        if goodBoi == 0:
            return 0

        days = -1
        while queue:
            days += 1
            for _ in range(len(queue)):
                locX, locY = queue.popleft()

                for nextX, nextY in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x, y = locX + nextX, locY + nextY

                    if 0 <= x < row and 0 <= y < col and grid[x][y] == 1:
                        grid[x][y] = 2
                        goodBoi -= 1
                        queue.append((x, y))

        return days if goodBoi == 0 else -1
