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
        removeNode, parent, isLeft = self.searchNode(root, value, None, False)

        if removeNode is None:
            return root

        newNode = None
        if removeNode.left is not None and removeNode.right is not None:
            newNode = self.popMin(removeNode.right)

            if removeNode.right and newNode != removeNode.right:
                newNode.right = removeNode.right
            else:
                newNode.right = None

            newNode.left = removeNode.left

            # print(newNode.right.val, newNode.left.val, newNode.val)
        elif removeNode.left is not None:
            newNode = removeNode.left
        elif removeNode.right is not None:
            newNode = removeNode.right

        if not parent:
            parent = newNode
            return parent
        elif isLeft:
            parent.left = newNode
        else:
            parent.right = newNode
        return root

    def searchNode(self, root, value, parent, isLeft):
        if not root:
            return None, parent, isLeft

        if value == root.val:
            return root, parent, isLeft
        elif value < root.val:
            return self.searchNode(root.left, value, root, True)
        else:
            return self.searchNode(root.right, value, root, False)

    def popMin(self, root):
        if not root:
            return root

        parent = root
        while root.left:
            parent = root
            root = root.left
        parent.left = None

        return root

# {1}
# 1
# {5,1}
# 5

# {20,1,40,#,#,35}
# 20

# {5,3,6,2,4}
# 3
