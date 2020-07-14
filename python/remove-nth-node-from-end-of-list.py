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
        n = 1 if n <= 1 else n
        # pop the first one?
        fake = ListNode(None, head)
        node = head
        stack = [fake]

        while node.next:
            stack.append(node)
            node = node.next

        for _ in range(n):
            node = stack.pop()

        if node.next:
            node.next = node.next.next

        return fake.next
