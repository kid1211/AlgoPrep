"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        # write your code here
        if not root:
            return node

        curr = root

        while curr != node:
            if node.val < curr.val:
                if not curr.left:
                    curr.left = node
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = node
                curr = curr.right
        return root
