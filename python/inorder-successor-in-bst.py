"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """

    def inorderSuccessor(self, root, p):
        # write your code here
        if not root:
            return None

        # if it value is on right subtree, it will be the left most one
        # other wise it can be the root or left

        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)

        left = self.inorderSuccessor(root.left, p)
        return left if left else root
