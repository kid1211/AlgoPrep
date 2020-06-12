#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # Decending array
        monoStack = []

        for num in nums:
            current = TreeNode(num)
            # if current is max, then need to pop all value out
            # last one that is pop is
            # the maximum of all the value that is smaller than current
            while monoStack and monoStack[-1].val < num:
                current.left = monoStack.pop()

            # the minimum value of all the value that is greater than current
            if monoStack:
                monoStack[-1].right = current

            monoStack.append(current)

        return monoStack[0]

        pass

    def constructMaximumBinaryTree2(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        curr = max(nums)
        idx = nums.index(curr)

        root = TreeNode(curr)
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx + 1:])
        return root
# @lc code=end
