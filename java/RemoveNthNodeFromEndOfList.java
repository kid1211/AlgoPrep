/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    // https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    // Iterative
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head == null || n < 1) return head;
        ListNode node = new ListNode(0);
        node.next = head;
        
        ListNode slow = node;
        ListNode fast = node;
        // Moving fast pointer n places first
        for(int i = 0; i <= n; ++i) {
            fast = fast.next; 
        }
        
        // Then move both the pointer one step till fast pointer
        // reaches null. At this point the slow pointer will be 
        // at the right spot, just one node before the node that
        // needs to get deleted.
        while(fast != null) {
            fast = fast.next;
            slow = slow.next;
        }
        
        slow.next = slow.next.next;
        return node.next;
    }
    
    /* Recursive
    private boolean endReached = false;
    private int count = 0;
    private ListNode removeNthUtil(ListNode head, int n) {
        if(head == null) {
            endReached = true;
            return head;
        }
        head.next = removeNthUtil(head.next, n);
        
        if(endReached) {
            count++;
            if(count == n) {
               return head.next; 
            }
        }
        
        return head;
    }
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head == null || n < 1) return head;
        return removeNthUtil(head, n);
    }
    */
}