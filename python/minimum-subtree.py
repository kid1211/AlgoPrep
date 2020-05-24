"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        # write your code here
        if not root:
            return root

        self.minimum = sys.maxsize
        self.resultNode = root

        self.dfs(root)
        return self.resultNode

    def dfs(self, root):
        if not root:
            return 0

        left_result = self.dfs(root.left)
        right_result = self.dfs(root.right)

        currentSum = left_result + right_result + root.val
        if currentSum < self.minimum:
            self.minimum = currentSum
            self.resultNode = root
        return currentSum


# {1,-5,2,1,2,-4,-5}
# {1,#,2}
