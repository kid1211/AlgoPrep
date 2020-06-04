#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        # get all the nodes
        nodeList = self.getNode(node)
        # create new node without neighbors in map
        nodeMap = {nd: Node(nd.val) for nd in nodeList}

        # add neighbor
        for nd in nodeList:
            newNode = nodeMap[nd]

            for neigh in nd.neighbors:
                newNeigh = nodeMap[neigh]
                newNode.neighbors.append(newNeigh)

        return nodeMap[node]

    def getNode(self, root):
        queue = deque([root])
        visited = set()
        rtn = []

        while queue:
            node = queue.popleft()
            if node in visited:
                continue

            visited.add(node)
            rtn.append(node)

            for neighbor in node.neighbors:
                queue.append(neighbor)
        return rtn
# @lc code=end
