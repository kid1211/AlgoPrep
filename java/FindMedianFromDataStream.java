class MedianFinder {
    // https://leetcode.com/problems/find-median-from-data-stream/
    PriorityQueue<Integer> left;
    PriorityQueue<Integer> right;
    
    /** initialize your data structure here. */
    public MedianFinder() {
        left = new PriorityQueue<>();
        
        right = new PriorityQueue<>(new Comparator<Integer>() {
            
            @Override
            public int compare(Integer a, Integer b) {
                return -Integer.compare(a, b);
            }
        });
        
    }
    
    public void addNum(int num) {
        left.offer(num);
        right.add(left.poll());
        if(left.size() < right.size()) {
            left.offer(right.poll());
        }
    }
    
    public double findMedian() {
        if(left.size() == 0) return 0;
        if(left.size() == right.size()) {
            return (left.peek() + right.peek()) / 2.0;
        } else {
            return (double)left.peek();
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */