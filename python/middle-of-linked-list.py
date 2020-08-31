"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """

    def middleNode(self, head):
        # write your code here.
        slow = ListNode(None, next=head)
        fast = ListNode(None, next=head)

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow.next if fast.next else slow
