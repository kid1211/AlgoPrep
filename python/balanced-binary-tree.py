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
        # write your code here
        isBalanced, _ = self.dfs(root, 0)
        return isBalanced

    def dfs(self, root, height):
        if not root:
            return True, height

        isLeftBalanced, leftH = self.dfs(root.left, height + 1)
        isRightBalanced, rightH = self.dfs(root.right, height + 1)

        if isLeftBalanced and isRightBalanced:
            return abs(leftH - rightH) <= 1, max(leftH, rightH)
        return False, None

# {1,2,3}
