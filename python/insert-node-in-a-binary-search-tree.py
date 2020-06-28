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
        temp = TreeNode(None)
        temp.left = root
        if not root:
            return node

        while root:
            # print(root.val)
            if node.val <= root.val:
                if not root.left:
                    root.left = node
                    break
                else:
                    root = root.left
            else:
                if not root.right:
                    root.right = node
                    break
                else:
                    root = root.right

        return temp.left
