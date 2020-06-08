#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#

# @lc code=start


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        graph = UnionFind(M)

        for row in range(len(M)):
            for col in range(len(M[row])):
                if M[row][col] == 0:
                    continue

                for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    point = (row + dx, col + dy)

                    if not self.isValid(M, point) or M[point[0]][point[1]] == 0:
                        continue

                    graph.union(point, (row, col))

        return graph.connected

    def isValid(self, M, point):
        return 0 <= point[0] < len(M) and 0 <= point[1] < len(M[0])


class UnionFind:
    def __init__(self, M):
        self.father = {}
        self.connected = 0

        for row in range(len(M)):
            for col in range(len(M[row])):
                self.father[(row, col)] = (row, col)

                if M[row][col] == 1:
                    self.connected += 1

    def find(self, point):
        path = []

        while self.father[point] != point:
            path += [point]
            point = self.father[point]

        for child in path:
            self.father[child] = point

        return point

    def union(self, point1, point2):
        root1, root2 = self.find(point1), self.find(point2)

        if root1 != root2:
            self.connected -= 1
            self.father[self.find(point1)] = self.find(point2)
# @lc code=end


2
