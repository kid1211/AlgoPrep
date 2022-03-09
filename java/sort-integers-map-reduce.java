// k 路归并的方法
class Element {
    public int row, col, val;
    Element(int row, int col, int val) {
        this.row = row;
        this.col = col;
        this.val = val;
    }
}

public class SortIntegers {

    public static class Map {
        public void map(int _, List<Integer> value,
                        OutputCollector<String, List<Integer>> output) {
            // Write your code here
            // Output the results into output buffer.
            // Ps. output.collect(String key, List<Integer> value);
            Collections.sort(value);
            output.collect("ignore_key", value);
        }
    }
        
    public static class Reduce {
        public void reduce(String key, List<List<Integer>> values,
                           OutputCollector<String, List<Integer>> output) {
            // Write your code here
            // Output the results into output buffer.
            // Ps. output.collect(String key, List<Integer> value);
            List<Integer> results = new ArrayList<Integer>();
            if (values.size() == 0) {
                output.collect(key, results);
                return;
            }
        
            int total_size = 0;

            Comparator<Element> ElementComparator = new Comparator<Element>() {
                public int compare(Element left, Element right) {
                    return left.val - right.val;
                }
            };

            Queue<Element> Q = new PriorityQueue<Element>(
                values.size(), ElementComparator);
            
            int k = values.size();
            for (int i = 0; i < k; i++) {
                if (values.get(i).size() > 0) {
                    Element elem = new Element(i, 0, values.get(i).get(0));
                    Q.add(elem);
                }
            }
        
            while (!Q.isEmpty()) {
                Element elem = Q.poll();
                results.add(elem.val);
                if (elem.col + 1 < values.get(elem.row).size()) {
                    elem.col += 1;
                    elem.val = values.get(elem.row).get(elem.col);
                    Q.add(elem);
                }
            }
        
            output.collect(key, results);
        }
    }
}