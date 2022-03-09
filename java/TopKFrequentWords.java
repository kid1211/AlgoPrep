class Solution {
    // https://leetcode.com/problems/top-k-frequent-words/
    public List<String> topKFrequent(String[] words, int k) {
    
        PriorityQueue<Map.Entry<String, Integer>> queue = new PriorityQueue<>(new Comparator<Map.Entry<String, Integer>>() {
            
            @Override
            public int compare(Map.Entry<String, Integer> a, Map.Entry<String, Integer> b) {
                if(a.getValue() == b.getValue()) {
                    return a.getKey().compareTo(b.getKey());
                }
                
                return -Integer.compare(a.getValue(), b.getValue());
            }
        });
        
        
        HashMap<String, Integer> map = new HashMap<>();
        
        for(String word : words) {
            map.put(word, map.getOrDefault(word, 0) + 1);
        }
        
        for(Map.Entry<String, Integer> entry : map.entrySet()) {
            queue.add(entry);
        }
        
        List<String> result = new ArrayList<>();
        
        while(k != 0) {
            Map.Entry<String, Integer> value = queue.poll();
            result.add(value.getKey());
            k--;
        }
        
        return result;
    }
}