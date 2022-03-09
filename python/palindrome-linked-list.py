# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        midNode, isOdd = self.findMid(head)

        if not midNode.next:
            return True

        # check if midNode.next exist
        midNode.next = self.reverse(midNode.next)
        # self.printLL(head)
        # print(midNode.val, isOdd)

        node1 = head
        node2 = midNode.next

        while node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next

        return not node2

    def findMid(self, head) -> (ListNode, bool):
        fast = ListNode(next=head)
        slow = ListNode(next=head)

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # isOdd == true when fast has no value
        return (slow, fast is None)

    def reverse(self, head):
        pre = None
        current = head
        nextN = head.next

        while nextN:
            current.next = pre

            pre = current
            current = nextN
            nextN = nextN.next

        current.next = pre
        return current

    def printLL(self, head):
        node = head
        res = ""
        while node:
            res += f"{node.val} ->"
            node = node.next

        print(res)
