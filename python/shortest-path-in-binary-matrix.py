class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        if grid[0][0] == 1:
            return -1

        ans = 0
        end = (len(grid) - 1, len(grid[0]) - 1)
        queue = collections.deque([(0, 0)])
        visited = set()

        while queue:
            ans += 1
            for _ in range(len(queue)):
                node = queue.popleft()

                if node == end:
                    return ans

                if node in visited:
                    continue
                visited.add(node)

                for dx, dy in [
                    (0, 1),
                    (1, 0),
                    (0, -1),
                    (-1, 0),
                    (1, 1),
                    (-1, -1),
                    (1, -1),
                    (-1, 1),
                ]:
                    x, y = node[0] + dx, node[1] + dy

                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
                        queue.append((x, y))

        return -1