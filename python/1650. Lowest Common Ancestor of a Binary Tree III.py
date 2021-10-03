"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
#                                 3
#                 5                                 1
#         6                2                   0           8
# 7               4

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()
        
        while p.parent and q.parent:
            if p == q:
                return p
            if p in visited:
                return p
            if q in visited:
                return q
            
            visited.add(p)
            visited.add(q)
            
            p = p.parent
            q = q.parent
        
        while p.parent :
            if p in visited:
                return p
            
            visited.add(p)
            p = p.parent
        
        while q.parent :
            if q in visited:
                return q
            
            visited.add(q)
            q = q.parent
        # return (visited)
        return p

# ver 2


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()
        # lastP
        
        while p.parent or q.parent:
            if p == q:
                return p
            if p in visited and p.parent is not None:
                return p
            if q in visited and q.parent is not None:
                return q
            
            visited.add(p)
            visited.add(q)
            
            if p.parent:
                p = p.parent
            if q.parent: 
                q = q.parent
                
        return p