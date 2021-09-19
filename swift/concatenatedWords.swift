class Solution {
    var memo = [String: Bool]()
    
    func findAllConcatenatedWordsInADict(_ words: [String]) -> [String] {
        var lookup = Set<String>()
        var res = Array<String>()
        let sorted = words.sorted { $0.count < $1.count }

        for word in sorted {
            if word.count == 0 {
                continue
            }
            
            if helper(word, lookup) {
                res += [word]
            }
            memo[word] = true
            lookup.insert(word)
        }
        
        return res
    }
    
    func helper(_ word: String, _ lookup: Set<String>) -> Bool {
        if let temp = memo[word] {
            return temp
        }
        
        if word.count == 0 {
            return true
        }
        
        for i in 1...word.count {
            let index = word.index(word.startIndex, offsetBy:i)
            let pre = String(word[word.startIndex..<index])
            
            if lookup.contains(pre) && helper(String(word[index..<word.endIndex]), lookup) {
                memo[word] = true
                return true
            }
        }
        
        memo[word] = false
        return false
    }
}