#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start


class Solution:
    def totalNQueens(self, n: int) -> int:
        results = []
        visited = {
            "col": set(),
            "sums": set(),
            "diff": set()
        }
        self.dfs([], visited, results, n)
        return len(results)

    def dfs(self, current, visited, results, n):
        row = len(current)

        if row == n:
            results.append(current)
            return

        for col in range(n):
            if not self.isValid(current, col, visited):
                continue

            visited["col"].add(col)
            visited["sums"].add(row + col)
            visited["diff"].add(row - col)
            current.append(col)
            self.dfs(current, visited, results, n)
            current.pop()
            visited["col"].remove(col)
            visited["sums"].remove(row + col)
            visited["diff"].remove(row - col)

    def isValid(self, current, col, visited):
        row = len(current)
        if col in visited['col']:
            return False
        if row + col in visited['sums']:
            return False
        if row - col in visited["diff"]:
            return False
        return True
# @lc code=end
