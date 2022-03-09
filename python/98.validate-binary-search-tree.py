#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        isValid, _, _ = self.dfs(root)
        return isValid

    def dfs(self, root):
        if not root:
            return True, None, None

        isLeft, leftMin, leftMax = self.dfs(root.left)
        isRight, rightMin, rightMax = self.dfs(root.right)

        if not isLeft or not isRight:
            return False, None, None

        if leftMin and not root.val > leftMax.val:
            return False, None, None
        if rightMax and not root.val < rightMin.val:
            return False, None, None

        leftMin = leftMin if leftMin is not None else root
        rightMax = rightMax if rightMax is not None else root
        return True, leftMin, rightMax
# @lc code=end
