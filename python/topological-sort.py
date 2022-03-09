"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
from collections import deque


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        indegrees = self.mapIndegrees(graph)
        # self.printMap(indegrees)

        # create a hash map for how many other node depend on itself
        # then start from the least dependency

        results = []
        queue = deque([node for node in indegrees if indegrees[node] == 0])

        while queue:
            node = queue.popleft()
            results.append(node)
            for neighbor in node.neighbors:
                # print(indegrees[neighbor])
                indegrees[neighbor] -= 1
                # print(indegrees[neighbor])
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        return results

    # return hash map
    def mapIndegrees(self, graph):
        rtn = {node: 0 for node in graph}

        for node in graph:
            for neighbour in node.neighbors:
                rtn[neighbour] += 1

        return rtn

    # def printMap(self, hashmap):
    #     for key, value in hashmap.items():
    #         print(f"{key.label}: {value}")
