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
    //     Recursive DFS 
    //     public TreeNode invertTree(TreeNode root) {
    //         if(root == null) return root;
            
    //         TreeNode moveRight = invertTree(root.left);
    //         TreeNode moveLeft = invertTree(root.right);
            
    //         root.left = moveLeft;
    //         root.right = moveRight;
            
    //         return root;
    //     }
        
    //      Iterative BFS
            public TreeNode invertTree(TreeNode root) {
                if(root == null) return root;
                Queue<TreeNode> queue = new LinkedList<>();
                queue.offer(root);
                while(!queue.isEmpty()) {
                    int size = queue.size();
                    
                    for(int i = 0; i < size; ++i) {
                        TreeNode node = queue.poll();
                        if(node == null) continue;
                        TreeNode temp = node.left;
                        node.left = node.right;
                        node.right = temp;
                        
                        queue.offer(node.left);
                        queue.offer(node.right);
                    }
                }
                return root;
            }
    }