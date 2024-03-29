class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        # write your code here
        if not root:
            return node

        if node.val >= root.val:
            if root.right:
                self.insertNode(root.right, node)
            else:
                root.right = node
        elif node.val < root.val:
            if root.left:
                self.insertNode(root.left, node)
            else:
                root.left = node

        return root
