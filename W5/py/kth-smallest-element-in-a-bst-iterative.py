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
        # on start
        node = root

        while True:
            while node:
                stack.append(node)
                node = node.left

            # at minimum
            if len(stack) <= 0:
                return -1

            node = stack.pop()
            k -= 1

            if k == 0:
                return node.val

            node = node.right

        return -5
        # stack = [root]
        # counter = 1
        # node = root

        # # in-order-traversal
        # while True:
        #     while node.left:
        #         stack.append(node)
        #         node = node.left

        #     if len(stack) == 0:
        #         break
        #     node = stack.pop()
        #     counter += 1
        #     if not node:
        #         break

        #     if counter >= k:
        #       return node.val

        #     node = node.right

        # return None
