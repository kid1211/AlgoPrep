"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree.
    @return: true if it is a complete binary tree, or false.
    """

    def isComplete(self, root):
        # write your code here
        if not root:
            return True
        queue = collections.deque([root])
        array = []

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                array.append(node)

                if node is not None:
                    queue.append(node.left)
                    queue.append(node.right)

        while array and array[-1] is None:
            array.pop()

        for item in array:
            if item is None:
                return False
        return True
