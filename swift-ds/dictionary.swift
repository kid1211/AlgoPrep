
class Trie {
    private class TrieNode {
        var children = [Character:TrieNode]()
        var isWord = false
    }
    private var root = TrieNode()

    init() {}
    
    func insert(_ word: String) {
        let word = Array(word)
        var node = root
        
        for c in word {
            node.children[c] = node.children[c, default: TrieNode()]
            node = node.children[c]!
        }
        
        node.isWord = true
    }
    
    private func find(_ word: String) -> TrieNode? {
        var node = root
        let word = Array(word)
        
        for c in word {
            guard let next = node.children[c] else { return nil }
            node = next
        }
        return node
    }
    
    func search(_ word: String) -> Bool {
        return find(word)?.isWord ?? false
    }
    
    func startsWith(_ prefix: String) -> Bool {
        return find(prefix) != nil
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * let obj = Trie()
 * obj.insert(word)
 * let ret_2: Bool = obj.search(word)
 * let ret_3: Bool = obj.startsWith(prefix)
 */

