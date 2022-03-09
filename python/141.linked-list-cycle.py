#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head

        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False

    def hasCycle2(self, head: ListNode) -> bool:
        visited = set()

        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False
# @lc code=end

# 59249269
