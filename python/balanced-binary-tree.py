"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        if not root:
            return True

        isBalanced, _ = self.dfs(root)
        return isBalanced

    def dfs(self, root):
        if not root:
            return True, 0

        isBalanced, leftHeight = self.dfs(root.left)
        if not isBalanced:
            return False, 0

        isBalanced, rightHeight = self.dfs(root.right)
        if not isBalanced:
            return False, 0

        return abs(rightHeight - leftHeight) <= 1, max(leftHeight, rightHeight) + 1


# {1,2,3,4,#,5,6,7,8,9,10,11,12}
#             1
#         2       3
# 4       #       5   6
