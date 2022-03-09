#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # hashset to keep track of visited
        row = len(grid)

        if row == 0:
            return 0

        col = len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]

        island = 0
        for i in range(row):
            for j in range(col):
                # check if it is island
                if self.isIsland(grid, visited, i, j):
                    island += 1
        return island

    def isIsland(self, grid, visited, row, col):
        # move right first

        # up, left, right, crap for extending the search
        # will start 0, 0 for row, col
        if not self.isSafe(grid, row, col) or grid[row][col] == "0" or visited[row][col]:
            return False

        visited[row][col] = True

        self.isIsland(grid, visited, row, col + 1)
        self.isIsland(grid, visited, row + 1, col)
        self.isIsland(grid, visited, row, col - 1)
        self.isIsland(grid, visited, row - 1, col)
        return True

    def isSafe(self, grid, row, col):
        maxRow = len(grid)
        # might need to check
        maxCol = len(grid[0])

        return row >= 0 and row < maxRow and col >= 0 and col < maxCol


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
