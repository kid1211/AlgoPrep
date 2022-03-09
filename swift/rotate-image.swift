class Solution {
    func rotate(_ matrix: inout [[Int]]) {
        let length = matrix.count
        
        for i in 0..<length {
            for j in (i + 1)..<length {
                let temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
            }
        }
        
        for i in 0..<length {
            matrix[i].reverse()
        }
    }
}
