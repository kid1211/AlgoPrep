"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        # write your code here
        res = []
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            res.append(str(node.val) if node else '#')

            if node:
                queue.append(node.left)
                queue.append(node.right)
        return '-'.join(res)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """

    def deserialize(self, data):
        # write your code here
        if not data:
            return None

        bfsNodes = [TreeNode(int(val)) if val !=
                    '#' else None for val in data.split('-')]
        n = len(bfsNodes)
        rootNodes = [bfsNodes[0]]
        i = 0
        j = 1

        while i < len(rootNodes) and j < n:
            node = rootNodes[i]
            node.left = bfsNodes[j]
            node.right = bfsNodes[j + 1]
            i += 1
            j += 2

            if node.left:
                rootNodes.append(node.left)
            if node.right:
                rootNodes.append(node.right)

        return rootNodes[0]
