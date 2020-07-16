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
        if not root or not target:
            return 0
        return self.findClosest(root, target)

    def findClosest(self, root, target):
        if not root:
            return sys.maxsize

        left = self.findClosest(root.left, target)
        right = self.findClosest(root.right, target)

        if root.val == target:
            return root.val
        elif root.val > target:
            # between left and root
            return root.val if abs(root.val - target) < abs(left - target) else left
        else:
            # between right and root
            return root.val if abs(root.val - target) < abs(right - target) else right
