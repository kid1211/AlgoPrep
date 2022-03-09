"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def invertBinaryTree(self, root):
        # write your code here
        self.dfs(root)

    def dfs(self, node):
        if not node:
            return

        node.right, node.left = node.left, node.right
        self.dfs(node.left)
        self.dfs(node.right)
