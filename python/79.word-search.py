class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        if not word:
            return True

        rows, cols = len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                if word[0] != board[i][j]:
                    continue
                startPoint = (i, j)
                if self.dfs(board, word, 0, startPoint, set([startPoint])):
                    return True
        return False

    def dfs(self, board, word, idx, startPoint, visited):
        n = len(word)
        if idx < n and word[idx] != board[startPoint[0]][startPoint[1]]:
            return False
        elif idx == n - 1:
            return True

        def isValid(x, y):
            return 0 <= x < len(board) and 0 <= y < len(board[0])

        x, y = startPoint
        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = (x + dx, y + dy)

            if (nx, ny) in visited or not isValid(nx, ny):
                continue

            visited.add((nx, ny))
            if self.dfs(board,  word, idx + 1, (nx, ny), visited):
                return True
            visited.discard((nx, ny))

        return False
