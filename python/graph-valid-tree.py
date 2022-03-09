class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # This is genius act
        # imagine a tree, also this catch an issue
        # when there is two part of a graph
        if len(edges) != n - 1:
            return False

        neighbors = collections.defaultdict(list)
        for left, right in edges:
            neighbors[left].append(right)
            neighbors[right].append(left)

        # because there is no direction, so no indegree
        # visited get out of cyclone, and catch graph node not being visited
        visited = set()
        queue = collections.deque([0])

        while queue:
            node = queue.popleft()
            visited.add(node)
            for edge in neighbors[node]:
                if edge in visited:
                    continue
                visited.add(edge)
                queue.append(edge)

        return len(visited) == n

# 10
# [[0,1],[5,6],[6,7],[9,0],[3,7],[4,8],[1,8],[5,2],[5,3]]


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)

        for e1, e2 in edges:
            uf.merge(e1, e2)

        return uf.connected == 1


class UnionFind:
    def __init__(self, n):
        self.connected = n
        self.father = {i: i for i in range(n)}

    def find(self, n):
        path = []

        while self.father[n] != n:
            path.append(n)
            n = self.father[n]

        for item in path:
            self.father[item] = n

        return n

    def merge(self, n1, n2):
        dad1, dad2 = self.find(n1), self.find(n2)

        if dad1 != dad2:
            self.connected -= 1
            self.father[dad1] = dad2
