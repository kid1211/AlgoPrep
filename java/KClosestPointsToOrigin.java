class Solution {
    // https://leetcode.com/problems/k-closest-points-to-origin/solution/
    private double getEuclideanDistance(int[] xy) {
        // Euclidean distance: c = ((xA − xB)^2 + (yA − yB)^2)^(1/2)
        return Math.sqrt(xy[0]*xy[0] + xy[1]*xy[1]); 
    }
    public int[][] kClosest(int[][] points, int K) {
        PriorityQueue<int[]> closestPoints = new PriorityQueue<>(K, new Comparator<int[]>() {
           @Override
            public int compare(int[] a, int[] b) {
                return Double.compare(getEuclideanDistance(a), getEuclideanDistance(b));
            }
        });
        
        
        for(int[] point: points) {
            closestPoints.offer(point);
        }
        
        int[][] result = new int[K][2];
        for(int i=0; i<K; ++i) {
            result[i] = closestPoints.poll();
        }
        
        return result;
    }
}