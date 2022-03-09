"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """

    def connectedSet(self, nodes):
        self.visited = set()

        res = []
        for node in nodes:
            if node in self.visited:
                continue
            current = []
            self.dfs(node, current)
            res.append(sorted(current))
        return res

    def dfs(self, node, res):
        self.visited.add(node)
        res.append(node.label)

        for node in node.neighbors:
            if node not in self.visited:
                self.dfs(node, res)


# union find
# go through all the nodes, and create the relationship based on it
