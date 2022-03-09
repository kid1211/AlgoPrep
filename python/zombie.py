class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid):
        rows = len(grid)
        if rows == 0:
            return -1
        cols = len(grid[0])

        humanCount, queue = self.init(grid, rows, cols)
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # print(humanCount)
        days = 0
        while queue:
            days += 1
            # print(queue)
            for _ in range(len(queue)):
                x, y = queue.popleft()
                # print((x,y))
                for dx, dy in steps:
                    nextStepX, nextStepY = x + dx, y + dy
                    if self.isHuman(grid, nextStepX, nextStepY):
                        grid[nextStepX][nextStepY] = 1
                        humanCount -= 1
                        queue.append((nextStepX, nextStepY))

        return -1 if humanCount != 0 else days - 1

    def init(self, grid, rows, cols):
        # return human count and queue withstarting poing
        humanCount = 0
        queue = collections.deque([])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    humanCount += 1
                elif grid[row][col] == 1:
                    # add to queue
                    queue.append((row, col))

        return humanCount, queue

    def isHuman(self, grid, row, col):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == 0

# [[0,1,2,0,0],
#  [1,0,0,2,1],
#  [0,1,0,0,0]]
