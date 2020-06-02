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
        return self.dfs(root, k1, k2)

    def dfs(self, root, k1, k2):
        if not root:
            return []

        rtn = []
        rtn += self.dfs(root.left, k1, k2)

        if root.val >= k1 and root.val <= k2:
            rtn.append(root.val)

        rtn += self.dfs(root.right, k1, k2)

        return rtn
