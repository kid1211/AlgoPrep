#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        visited = {
            "col": set(),
            "sums": set(),
            "diff": set()
        }
        self.dfs([], results, visited, n)
        return results

    def dfs(self, permutation, results, visited, n):
        # print(permutation)
        if len(permutation) == n:
            # drawboard
            results.append(self.draw_board(permutation))
            return

        row = len(permutation)
        for col in range(n):
            if not self.isValid(row, col, visited):
                continue

            visited["diff"].add(row - col)
            visited["sums"].add(row + col)
            visited["col"].add(col)
            permutation.append(col)
            # [".Q..", "...Q", "Q...", "..Q."]
            self.dfs(permutation, results, visited, n)
            permutation.pop()
            visited["col"].remove(col)
            visited["sums"].remove(row + col)
            visited["diff"].remove(row - col)

    def draw_board(self, current):
        # current is going to be an n lenght of interger [1,2,3,4]
        results = []
        for row in current:
            results.append(
                "".join(['Q' if i == row else '.' for i in range(len(current))])
            )
        return results

    def isValid(self, row, col, visited):
        if col in visited["col"]:
            return False
        if (row + col) in visited["sums"]:
            return False
        if row - col in visited["diff"]:
            return False
        return True


# @lc code=end
[['.', 'Q', '.'], ['.', '.', 'Q'], ['.', '.', '.']]
