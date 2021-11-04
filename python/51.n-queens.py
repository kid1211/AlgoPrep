cols = "COLS"
sums = "SUMS"
diff = "DIFF"


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visited = {
            cols: set(),
            sums: set(),  # postive slope
            diff: set(),  # negative slope
        }

        results = []
        self.dfs([], results, visited, n)
        return results

    def dfs(self, curr, results, visited, n):
        if len(curr) == n:
            results += [self.drawBoards(curr, n)]
            return

        row = len(curr)
        for col in range(n):
            if (
                col in visited[cols]
                or (col + row) in visited[sums]
                or (col - row) in visited[diff]
            ):
                continue

            visited[cols].add(col)
            visited[sums].add(col + row)
            visited[diff].add(col - row)
            self.dfs(curr + [col], results, visited, n)
            visited[cols].remove(col)
            visited[sums].remove(col + row)
            visited[diff].remove(col - row)

    def drawBoards(self, current, n):
        # current is going to be an n lenght of interger [1,2,3,4]
        # indicate which col has Q
        res = []
        for col in current:
            res += ["".join(["Q" if i == col else "." for i in range(n)])]

        return res
