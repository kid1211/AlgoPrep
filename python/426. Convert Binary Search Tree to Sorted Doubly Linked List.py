"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.first = None
        self.prev = None
        self.dfs(root)
        # as
        self.prev.right = self.first
        self.first.left = self.prev
        return self.first
    
    def dfs(self, root):
        if not root:
            return
        
        self.dfs(root.left)
        
        if self.prev:
            self.prev.right = root
            root.left = self.prev
        else:
            """
            first ever node (smallest) would not have prev
            """
            self.first = root
        
        self.prev = root
        self.dfs(root.right)
        
        return root