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
    // https://leetcode.com/problems/insert-into-a-binary-search-tree/
    public TreeNode insertIntoBST(TreeNode root, int val) {
   
        // Iterative
        TreeNode node = root;
        TreeNode newNode = new TreeNode(val);
        while(node != null) {
            if(val < node.val) {
                if(node.left == null) {
                    node.left = newNode;
                    return root;
                }
                node = node.left;
            } else {
                if(node.right == null) {
                    node.right = newNode;
                    return root;
                }
                node = node.right;
            }
        }
        
        return newNode;
        
        // Recursive
//         if(root == null) return new TreeNode(val);
        
//         if(val < root.val) {
//             root.left = insertIntoBST(root.left, val);
//         } else {
//             root.right = insertIntoBST(root.right, val);
//         }
        
//         return root;
    }
}