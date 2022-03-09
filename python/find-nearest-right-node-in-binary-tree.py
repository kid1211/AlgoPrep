# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        queue = collections.deque([root])
        
        ans = None
        while queue:
            current = []
            for _ in range(len(queue)):
                node = queue.popleft()
                current.append(node)
                
                if node == u:
                    ans = len(current)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            if ans:
                return current[ans] if ans < len(current) else None
        return None