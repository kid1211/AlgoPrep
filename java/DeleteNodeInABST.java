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
    // https://leetcode.com/problems/delete-node-in-a-bst/solution/
    private TreeNode getSuccessor(TreeNode node) {
        if(node == null) return null;
        while(node.left != null) {
            node = node.left;
        }
        return node;
    } 
    
    private TreeNode getPredecessor(TreeNode node) {
        if(node == null) return null;
        while(node.right != null) {
            node = node.right;
        }
        return node;
    }
    
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;
        
        if(key < root.val) {
            // System.out.println("left");
            root.left = deleteNode(root.left, key);
        } else if(key > root.val) {
            // System.out.println("right");
            root.right = deleteNode(root.right, key);
        } else {
            // System.out.println("match: " + root.val);
            if(root.left == null && root.right == null) return null;
            
            if(root.right != null) {
                // System.out.println("match right");
                TreeNode successor = getSuccessor(root.right);
                deleteNode(root, successor.val);
                successor.right = root.right;
                successor.left = root.left;
                // System.out.println(successor.val);
                return successor;
            }
            
            if(root.left != null) {
                TreeNode predecessor = getPredecessor(root.left);
                deleteNode(root, predecessor.val);
                predecessor.left = root.left;
                // System.out.println(predecessor.val);
                return predecessor;
            }
        }
        return root;
    }
}