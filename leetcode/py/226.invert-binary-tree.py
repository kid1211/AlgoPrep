#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # left, right root travers

        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return
        print(root.val)
        leftNode = self.dfs(root.left)
        rightNode = self.dfs(root.right)

        root.left, root.right = rightNode, leftNode
        return root
# @lc code=end


my
[4, 2, 7, 1, 3, 6, 9]
expect
[4, 7, 2, 9, 6, 3, 1]
