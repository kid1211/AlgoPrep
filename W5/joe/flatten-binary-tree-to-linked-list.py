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
        if not root:
            return root

        leftNode = self.flatten(root.left)
        rightNode = self.flatten(root.right)

        if not rightNode:
            root.right = leftNode
            root.left = None
        if not leftNode:
            return root
        else:
            mostRightFromLeft = leftNode
            while mostRightFromLeft.right:
                mostRightFromLeft = mostRightFromLeft.right
            mostRightFromLeft.right = rightNode
            root.right = leftNode
            root.left = None

        return root
