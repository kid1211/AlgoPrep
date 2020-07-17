"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """

    def numIslands2(self, n, m, operators):
        # write your code here
        uf = UnionFind(n, m)

        res = []
        for pt in operators:
            if 0 <= pt.x < n and 0 <= pt.y < m:
                res.append(uf.addIsland(pt))

        return res


class UnionFind:
    def __init__(self, n, m):
        self.island = 0  # debatable
        self.father = {}

    def addIsland(self, pt):
        x, y = pt.x, pt.y

        if (x, y) in self.father:
            return self.island

        self.father[(x, y)] = (x, y)
        self.island += 1

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newPt = (x + dx, y + dy)

            if newPt in self.father:
                self.union((x, y), newPt)

        return self.island

    def find(self, pt):
        path = []

        while self.father[pt] != pt:
            path.append(pt)
            pt = self.father[pt]

        for ele in path:
            self.father[ele] = pt

        return pt

    def union(self, pt1, pt2):
        dad1, dad2 = self.find(pt1), self.find(pt2)

        if dad1 != dad2:
            self.island -= 1  # self.island shoudl never be 0 before -= 1
            self.father[dad1] = dad2
