# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.dfs(root, 0)[0]

    def dfs(self, root, height):
        if not root:
            return root, height

        leftNode, leftHeight = self.dfs(root.left, height + 1)
        rightNode, rightHeight = self.dfs(root.right, height + 1)

        if leftHeight == rightHeight:
            return root, leftHeight

        if leftHeight > rightHeight:
            return leftNode, leftHeight
        else:
            return rightNode, rightHeight
