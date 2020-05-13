#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # hashset to keep track of visited
        count = 0
        row = len(grid)

        if row == 0:
            return 0

        col = len(grid[0])

        visited = [[False for _ in range(col)] for _ in range(row)]

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '0' or visited[row][col]:
                    continue

                visited[row][col] = True
                count += 1
                queue = deque([(row, col)])

                while queue:
                    node = queue.popleft()
                    for (dx, dy) in directions:
                        nRow, nCol = node[0] + dx, node[1] + dy
                        if self.isValid(grid, nRow, nCol) and grid[nRow][nCol] == '1' and not visited[nRow][nCol]:
                            visited[nRow][nCol] = True
                            queue.append((nRow, nCol))
        return count

    def isValid(self, grid, row, col):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[row])


# @lc code=end
[
    [["1", "1", "1"],
     ["0", "1", "0"],
     ["1", "1", "1"]]
]

[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

[
    ["1", "0", "1", "1", "0", "1", "1"]
]
