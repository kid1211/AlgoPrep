class Solution {
    
    private int[] parent;
    private int[] size;
    private int groups;
    
    private void initialize(int friendsCount) {
        parent = new int[friendsCount];
        size = new int[friendsCount];
        groups = friendsCount;
        for(int i=0; i<friendsCount; ++i) {
            parent[i] = i;
            size[i] = 1;
        }
    }
    
    private int find(int friend) {
        while(friend != parent[friend]) {
            friend = parent[friend];
        }
        return friend;
    }
    
    private void union(int friendX, int friendY) {
        int friendXParent = find(friendX);
        int friendYParent = find(friendY);
        
        if(friendXParent == friendYParent) return;
        
        groups--;
        if(size[friendXParent] < size[friendYParent]) {
            parent[friendXParent] = friendYParent;
            size[friendYParent] += size[friendXParent];
        } else {
            parent[friendYParent] = friendXParent;
            size[friendXParent] += size[friendYParent];
        }
    } 
    
    public int findCircleNum(int[][] M) {
        initialize(M.length);
        for(int i=0; i<M.length; ++i) {
            for(int j=0; j<M.length; ++j) {
                if(M[i][j] == 1 && i != j) {
                    union(i, j);
                }
            }
        }
        return groups;
    }
}