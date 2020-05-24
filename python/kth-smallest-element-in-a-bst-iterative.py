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

        stack = []
        # dummy = TreeNode(0)
        # dummy.right = root

        # on start
        node = root

        for i in range(k - 1):
            while node:
                stack.append(node)
                node = node.left
            # at minimum
            if len(stack) <= 0:
                return None

            node = stack.pop()
            # k -= 1

            # if k == 0:
            #     return node.val

            node = node.right
        print(stack)

        while node:
            stack.append(node)
            node = node.left
        return stack[-1].val
