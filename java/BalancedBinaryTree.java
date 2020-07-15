/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    // https://leetcode.com/problems/balanced-binary-tree/
    private boolean balanced = true;
    private int isBalancedUtil(TreeNode node) {
        if(node == null || !balanced) return 0;
        
        int left = isBalancedUtil(node.left) + 1;
        int right = isBalancedUtil(node.right) + 1;
        
        if(Math.abs(right - left) > 1) balanced = false;
        
        return Math.max(left, right);
    }
    public boolean isBalanced(TreeNode root) {
        isBalancedUtil(root);
        return balanced;
    }
}