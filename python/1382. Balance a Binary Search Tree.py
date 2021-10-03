# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.sorted = []
        self.dfs(root)
        for node in self.sorted:
            print(node.val)
        
        return self.buildTree(self.sorted)
    def dfs(self, root):
        if not root:
            return
        
        self.dfs(root.left)
        self.sorted += [root]
        self.dfs(root.right)
    
    def buildTree(self, arr):
        if not arr:
            return None
        
        mid = len(arr) // 2
        
        left = self.buildTree(arr[:mid])
        right = self.buildTree(arr[mid+1:])
        
        node = arr[mid]
        
        node.left = left
        node.right = right
        return node