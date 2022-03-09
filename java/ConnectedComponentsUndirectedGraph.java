class Solution {
    // https://leetcode.com/accounts/login/?next=/problems/number-of-connected-components-in-an-undirected-graph/
    private int[] unionFind;
    private int components;
    
    private void initialize(int n) {
        unionFind = new int[n];
        components = n;
        for(int i=0; i<n; ++i) {
            unionFind[i] = i;
        }
    }
    
    private void union(int vertexOne, int vertexTwo) {
        int parentOne = findComponentParent(vertexOne);
        int parentTwo = findComponentParent(vertexTwo);
        
        if(parentOne != parentTwo) {
            // System.out.println("One: " + parentOne + " | two: " + parentTwo);
            unionFind[parentTwo] = parentOne;
            components--;
        }
    }
    
    private int findComponentParent(int vertex) {       
        while(vertex != unionFind[vertex]) {
            unionFind[vertex] = unionFind[unionFind[vertex]];
            vertex = unionFind[vertex];
        }
        return vertex;
    }
    
    public int countComponents(int n, int[][] edges) {
        initialize(n);
        
        for(int[] edge : edges) {
            union(edge[0], edge[1]);
        }
        
        return components;
    }
}