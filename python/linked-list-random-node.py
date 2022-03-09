# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.length = 1
        self.head = head

        node = head
        while node.next:
            self.length += 1
            node = node.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        if self.length == 0:
            return None

        from random import randrange
        rand = randrange(self.length)
        node = self.head
        while rand > 0:
            node = node.next
            rand -= 1
        return node.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

# save prev node in an arry
