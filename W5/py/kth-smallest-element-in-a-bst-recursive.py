"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):
        # write your code here
        # find the smallest and come back
        smallest = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            smallest.append(node.val)
            dfs(node.right)

        dfs(root)

        return smallest[k - 1]
