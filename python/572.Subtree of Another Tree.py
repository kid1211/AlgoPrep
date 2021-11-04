# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return False

        return (
            self.isSameTree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    def isSameTree(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False

        if root.val != subRoot.val:
            return False
        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(
            root.right, subRoot.right
        )

