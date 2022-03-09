/**
 * Definition of Interval:
 * public classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */
// https://www.lintcode.com/problem/merge-k-sorted-interval-lists/description
public class Solution {
    
    private class Pair {
        public int row;
        public int col;
    
        public Pair(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
    
    /**
     * @param intervals: the given k sorted interval lists
     * @return:  the new sorted interval list
     */
    public List<Interval> mergeKSortedIntervalLists(List<List<Interval>> intervals) {
        // write your code here
        
        PriorityQueue<Pair> pq = new PriorityQueue<>(new Comparator<Pair>() {
            @Override
            public int compare(Pair left, Pair right) {
                return Integer.compare(intervals.get(left.row).get(left.col).start,
                    intervals.get(right.row).get(right.col).start);
            }
        });
        
        
        for(int i = 0; i < intervals.size(); ++i) {
            if(intervals.get(i).size() > 0) {
                pq.offer(new Pair(i,0));
            }
        }
        
        List<Interval> sortedIntervals = new ArrayList<>();
        while(!pq.isEmpty()) {
            Pair pair = pq.poll();
            
            sortedIntervals.add(intervals.get(pair.row).get(pair.col));
            
            if(pair.col < intervals.get(pair.row).size() - 1) {
                pq.offer(new Pair(pair.row, pair.col + 1));
            }
        }
        
        List<Interval> result = new ArrayList<>();
        result.add(sortedIntervals.get(0));
        
        for(int i = 1; i < sortedIntervals.size(); ++i) {
            Interval previous = result.get(result.size() - 1);
            Interval current = sortedIntervals.get(i);
            int end;
            if(previous.end >= current.start) {
                previous.end = Math.max(previous.end, current.end);
            } else {
                result.add(current);
            }
        }
        
        return result;
    }
}