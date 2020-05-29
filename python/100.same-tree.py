#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.dfs(p, q)

    def dfs(self, p, q):
        if p == None or q == None:
            return p == q

        if p.val != q.val:
            return False

        if self.dfs(p.left, q.left) == False:
            return False

        if self.dfs(p.right, q.right) == False:
            return False

        return True
# @lc code=end
