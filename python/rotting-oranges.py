class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        goodies = set()

        init = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    init.append((i, j))
                elif grid[i][j] == 1:
                    goodies.add((i, j))

        queue = collections.deque(init)

        count = -1
        while queue:
            count += 1
            for _ in range(len(queue)):
                rotten_x, rotten_y = queue.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x, y = rotten_x + dx, rotten_y + dy

                    if (x, y) in goodies:
                        goodies.remove((x, y))
                        queue.append((x, y))

        if count == -1 and goodies:
            return -1
        count = 0 if count == -1 else count
        return -1 if goodies else count
