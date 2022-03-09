"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """

    def removeNode(self, root, value):
        removeNode, parent, isLeft = self.search(root, value)

        if removeNode is None:
            return root

        # if it is leaf node then good
        # if one side is missing, just move it up
        # else look at below

        newNode = None
        if removeNode.right and removeNode.left:
            # find the min from its right child to replace head
            # to replace remove Node, this will keep BST
            newNode = self.popMin(removeNode.right)

            # if the smallest is not the right child we need its right child
            # other wise it is already taken care of
            if newNode != removeNode.right:
                newNode.right = removeNode.right

            # carry over the left child from remove Node
            newNode.left = removeNode.left

        elif removeNode.left:
            newNode = removeNode.left
        elif removeNode.right:
            newNode = removeNode.right

        # replace removed Node with newNode
        # print(removeNode, parent, isLeft)
        if not parent:
            return newNode
        elif isLeft:
            parent.left = newNode
        else:
            parent.right = newNode
        return root

    def search(self, root, value):
        parent = root
        isLeft = False
        while root:
            if root.val == value:
                # prevent no travers
                parent = None if parent == root else parent
                return root, parent, isLeft
            elif root.val > value:
                parent = root
                root = root.left
                isLeft = True
            else:
                parent = root
                root = root.right
                isLeft = False

        return None, None, False

    def popMin(self, node):
        if not node:
            return node

        parent = node
        while node.left:
            parent = node
            node = node.left

        parent.left = None
        return node
