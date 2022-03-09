class Solution {

    private List<List<String>> result = new ArrayList<>();
    
    private boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        
        while(left < right) {
            if(s.charAt(left) != s.charAt(right)) return false;
            left++;
            right--;
        }
        return true;
    }
    
    private void backtrack(String s, int start, List<String> partitions) {
        if(start == s.length()) {
            result.add(new ArrayList<>(partitions));
            return;
        }
        
        for(int i=start; i < s.length(); ++i) {
            String currString = s.substring(start, i+1);
            if(isPalindrome(currString)) {
                partitions.add(currString);
                backtrack(s, i+1, partitions);
                partitions.remove(partitions.size() - 1);
            }
        }
    }
    
    public List<List<String>> partition(String s) {
        
        backtrack(s, 0, new ArrayList<>());
        
        return result;
    }
}