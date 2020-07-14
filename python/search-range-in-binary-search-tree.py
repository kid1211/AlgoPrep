"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        # write your code here
        res = []
        # pre-order-traverse
        self.dfs(root, k1, k2, res)
        return res

    def dfs(self, root, k1, k2, res):
        if not root:
            return

        self.dfs(root.left, k1, k2, res)
        if k1 <= root.val <= k2:
            res.append(root.val)
        self.dfs(root.right, k1, k2, res)
