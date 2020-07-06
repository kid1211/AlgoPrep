class Solution {
    // https://leetcode.com/problems/decode-string/
    public String decodeString(String s) {
        Stack<Integer> numbers = new Stack<>();
        Stack<String> chars = new Stack<>();
        String currString = "";
        int i = 0;
        while(i < s.length()) {
            if (Character.isDigit(s.charAt(i))) {
                int num = 0;
                while(Character.isDigit(s.charAt(i))) {
                    num = (num * 10) + (s.charAt(i) - '0');
                    ++i;
                }
                numbers.push(num);
            } else if (s.charAt(i) == '[') {
                chars.push(currString);
                currString = "";
                i++;
            } else if( s.charAt(i) == ']') {
                StringBuilder str = new StringBuilder(chars.pop());
                int num = numbers.pop();
                for(int j=0; j<num; ++j) {
                    str.append(currString);
                }
                currString = str.toString();
                ++i;
            } else {
                currString += s.charAt(i);
                ++i;
            }
        }
      return currString;
    }
}