"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        if not headA or not headB:
            return None
        
        pt1, pt2 = headA, headB
        
        while pt1 != pt2:
            pt1 = pt1.next if pt1 else headB
            pt2 = pt2.next if pt2 else headA
        
        return pt1