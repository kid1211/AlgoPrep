public class Solution {
    // https://www.lintcode.com/problem/anagrams/description
    HashMap<String, List<String>> map = new HashMap<>();
    /**
     * @param strs: A list of strings
     * @return: A list of strings
     */
    public List<String> anagrams(String[] strs) {
        // write your code here
        
        for(String str : strs) {
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            String sorted = String.valueOf(charArray);
            if(!map.containsKey(sorted)) {
                List<String> list = new ArrayList<>();
                list.add(str);
                map.put(sorted, list);
            } else {
                List<String> list = map.get(sorted);
                list.add(str);
            }
        }
        
        List<String> result = new ArrayList<>();
        for(List<String> list : map.values()) {
            if(list.size() > 1) {
                result.addAll(list);
            }
        }
        return result;
    }
}