#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # if word
        self.rows = len(board)
        if self.rows == 0:
            return False
        self.cols = len(board[0])

        for row in range(self.rows):
            for col in range(self.cols):
                if board[row][col] != word[0]:
                    continue
                startPoint = (row, col)
                if self.dfs(board, word, startPoint, set([startPoint])):
                    return True
        return False

    def dfs(self, board, word, startPoint, visited):
        if len(word) == 0:
            return True

        if word[0] != board[startPoint[0]][startPoint[1]]:
            return False

        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nextPoint = (startPoint[0] + dx, startPoint[1] + dy)

            if nextPoint in visited:
                continue

            if not self.isValid(nextPoint):
                continue

            # print("mid " + word, visited, startPoint, (dx, dy))
            visited.add(nextPoint)

            if self.dfs(board, word[1:], nextPoint, visited):
                return True

            visited.remove(nextPoint)

        return len(word) == 1

    def isValid(self, nextPoint):
        return 0 <= nextPoint[0] < self.rows and 0 <= nextPoint[1] < self.cols


# @lc code=end
[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]\n"ABCB"

[["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]] \ n"AAB"

[["a"]]\n"a"
