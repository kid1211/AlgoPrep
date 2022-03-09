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

    def flatten(self, root):
        # write your code here
        self.dfs(root)

    # connect and return last node in the subtree
    def dfs(self, root):
        if not root:
            return None

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left:
            left.right = root.right
            root.right = root.left
            root.left = None

        return right or left or root
