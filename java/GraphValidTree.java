public class Solution {
    // https://www.lintcode.com/problem/graph-valid-tree/description
    // Approach: union find to detect cycles
    private int[] unionFind;
    private int unions;
    
    private void initialize(int n) {
        unionFind = new int[n];
        for(int i = 0; i < n; ++i) {
            unionFind[i] = i;
        }
    }
    
    private int find(int node) {
        int parent;
        while(node != unionFind[node]) {
            parent = unionFind[unionFind[node]];
            unionFind[node] = parent;
            node = parent;
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
            if(!success) return false;
        }
        
        return unions == n-1;
    }
}