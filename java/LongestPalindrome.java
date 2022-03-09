public class Solution {
    // https://www.lintcode.com/problem/longest-palindrome/description
    /**
     * @param s: a string which consists of lowercase or uppercase letters
     * @return: the length of the longest palindromes that can be built
     */
    public int longestPalindrome(String s) {
        // write your code here

        HashSet<Character> set = new HashSet<>();
        
        for(char c: s.toCharArray()) {
            if(set.contains(c)) {
                set.remove(c);
            } else {
                set.add(c);
            }
        }
        
        int singleChars = set.size();
        
        if(singleChars > 0) {
            singleChars--;
        }
        
        return s.length() - singleChars;

        // HashMap<Character, Integer> map = new HashMap<>();
        
        // for(char c: s.toCharArray()) {
        //     map.put(c, map.getOrDefault(c, 0) + 1);
        // }

        // int pair = 0;
        // int single = 0;
        
        // for(int count : map.values()) {
        //     int div = count / 2;
        //     pair += div;
        //     single += count % 2;
        // }
        
        // return (pair * 2) + (single > 0 ? 1 : 0);
    }
}