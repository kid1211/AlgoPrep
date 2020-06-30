public class Solution {
    
    private int[] unionFind;
    private int unions;
    
    private void initialize(int n) {
        unionFind = new int[n];
        for(int i = 0; i < n; ++i) {
            unionFind[i] = i;
        }
    }
    
    private int find(int node) {
        // System.out.println("node: " + node + " | " + Arrays.toString(unionFind));
        
        // System.out.println("unionFind[node]: " + unionFind[node]);
        while(node != unionFind[node]) {
            // System.out.println("node: " + node);
            node = unionFind[unionFind[node]];
        }
        return node;
    }
    
    private boolean union(int left, int right) {
        int leftParent = find(left);
        int rightParent = find(right);
        
        if(leftParent == rightParent) return false;
        
        unionFind[rightParent] = leftParent;
        unions++;
        return true;
    }
    
    /**
     * @param n: An integer
     * @param edges: a list of undirected edges
     * @return: true if it's a valid tree, or false
     */
    public boolean validTree(int n, int[][] edges) {
        // write your code here
        
        if(edges.length == 0 && n > 1) return false;
        
        initialize(n);
        for(int[] edge : edges) {
            boolean success = union(edge[0], edge[1]);
            // System.out.println("bool: " + success + " | 0: " + edge[0] + " | 1: " + edge[1]);
            if(!success) return false;
        }
        
        return unions == n-1;
    }
}