# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        root = ListNode()
        ans = root
        node1 = l1
        node2 = l2
        carryOver = 0

        while node1 or node2:
            node1Val = node1.val if node1 else 0
            node2Val = node2.val if node2 else 0

            addition = node1Val + node2Val + carryOver
            carryOver = math.floor(addition / 10)
            ans.next = ListNode(addition % 10)

            ans = ans.next
            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None

        if carryOver != 0:
            ans.next = ListNode(carryOver)

        return self.reverse(root.next)

    def reverse(self, node):
        prev = None
        curr = node
        nextN = curr.next

        while nextN:
            curr.next = prev

            prev = curr
            curr = nextN
            nextN = nextN.next

        curr.next = prev
        return curr
