"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):
        # write your code here
        if not target:
            return 0
        return self.dfs(root, target)

    def dfs(self, root, target):
        if not root:
            return sys.maxsize

        left = self.dfs(root.left, target)
        right = self.dfs(root.right, target)

        def getClosest(val):
            return val if abs(val - target) < abs(root.val - target) else root.val

        if root.val == target:
            return root.val
        elif root.val > target:
            return getClosest(left)
        else:
            return getClosest(right)
