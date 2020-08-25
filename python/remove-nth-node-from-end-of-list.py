"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """

    def removeNthFromEnd(self, head, n):
        # write your code here
        stack = []

        node = head
        while node.next:
            stack.append(node)
            node = node.next

        for _ in range(n - 1):
            node = stack.pop()

        if not stack:
            return head.next
        prev = stack.pop()
        prev.next = node.next
        return head


# let quick pointer go for n first then continue


# def removeNthFromEnd(self, head, n):
#     res = ListNode(0)
#      res.next = head
#       tmp = res
#        for i in range(0, n):
#             head = head.next
#         while head != None:
#             head = head.next
#             tmp = tmp.next
#         tmp.next = tmp.next.next
#         return res.next
