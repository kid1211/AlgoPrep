class Solution {    
    private TrieNode root;
    private List<List<String>> result = new ArrayList<>();
    
    private class TrieNode {
        public boolean isWord;
        public TrieNode[] chars;
        public char value;
        
        public TrieNode() {
            this('0', false);    
        }
        
        public TrieNode(char value, boolean isWord) {
            this.value = value;
            this.isWord = isWord;
            chars = new TrieNode[26];
        }
    }
    
    private void insert(String word) {
        TrieNode node = root;
        
        for(int i=0; i < word.length(); ++i) {
            int currentCharIndex = word.charAt(i) - 'a';
            if(node.chars[currentCharIndex] == null) {
                TrieNode charNode = new TrieNode(word.charAt(i), false);
                node.chars[currentCharIndex] = charNode;
                node = charNode;
            } else {
                node = node.chars[currentCharIndex];
            }
        }
        node.isWord = true;
    }
    
    private TrieNode findPrefixNode(String prefix) {
        TrieNode node = root;
        
        for(int i = 0; i < prefix.length(); ++i) {
            int currentCharIndex = prefix.charAt(i) - 'a';
            if(node.chars[currentCharIndex] == null) return null;
            
            node = node.chars[currentCharIndex];
        }
        
        return node;
    }
    
    private List<String> getSuggestedWords(String prefix, TrieNode prefixNode, List<String> suggestedWords) {
        TrieNode[] chars = prefixNode.chars;
        for(int i = 0; i < chars.length; ++i) {
            if(suggestedWords.size() == 3) return suggestedWords;
            if(chars[i] != null) {
                TrieNode node = chars[i];
                String word = prefix + node.value;
                if(node.isWord) suggestedWords.add(word);
                getSuggestedWords(word, node, suggestedWords);
            }
        }
        return suggestedWords;
    }
    
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {      
        root = new TrieNode();
        for(String product : products) {
            insert(product);
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < searchWord.length(); ++i) {
            List<String> suggestedWords = new ArrayList<>();
            String prefix = sb.append(searchWord.charAt(i)).toString();
            TrieNode prefixNode = findPrefixNode(prefix);
            if(prefixNode == null) {
                result.add(suggestedWords);
                continue;
            };
            if(prefixNode.isWord) suggestedWords.add(prefix);
            suggestedWords = getSuggestedWords(prefix, prefixNode, suggestedWords);
            result.add(suggestedWords);
        }
        
        return result;
    }
}