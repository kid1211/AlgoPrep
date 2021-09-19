class Solution {
    func longestPalindrome(_ s: String) -> String {
        var convertedS = "#"
        for char in s {
            convertedS += [char]
            convertedS += ["#"]
        }

        var longest = ""
        for i in 0..<convertedS.count {
            let curr = getLongestPalindrome(convertedS, i)
            if curr.count > longest.count {
                longest = curr
            }
        }
        
        return longest.replacingOccurrences(of: "#", with: "")
    }
    
    func getLongestPalindrome(_ s: String, _ i: Int) -> String {
        var leftI = i, rightI = i
        
        func getIndex(_ i: Int) -> String.Index {
            return s.index(s.startIndex, offsetBy: i)
        }
        
        while s[getIndex(leftI)] == s[getIndex(rightI)] {
            guard (leftI - 1 >= 0) && (rightI + 1 < s.count) else {
                return String(s[getIndex(leftI)...getIndex(rightI)])
            }
            
            leftI -= 1
            rightI += 1
        }
        return String(s[getIndex(leftI + 1) ..< getIndex(rightI)])
    }
}