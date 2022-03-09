class Solution {
    func canFinish(_ numCourses: Int, _ prerequisites: [[Int]]) -> Bool {
        var (indegree, mapping) = buildMap(numCourses, prerequisites)
        var deque = indegree.filter { $0.value == 0 }.map { $0.key }
        
        var res: [Int] = []
        
        while deque.count > 0 {
            let node = deque.removeFirst()
            res += [node]
            
            for next in mapping[node]! {
                indegree[next]! -= 1
                if indegree[next] == 0 {
                    deque += [next]
                }
            }
        }
        
        return res.count == numCourses
    }
    
    private func buildMap(_ numCourses: Int, _ prerequisites: [[Int]]) -> ([Int: Int], [Int: [Int]]) {
        var indegree:[Int: Int] = [:]
        var mapping:[Int: [Int]] = [:]
        
        for i in 0..<numCourses {
            indegree[i] = 0
            mapping[i] = []
        }
        
        for require in prerequisites {
            let pre = require[0]
            let post = require[1]
            
            indegree[post]! += 1
            mapping[pre]! += [post]
        }
        
        return (indegree, mapping)
    }
}

// class Deque<T> {
//     var ele: T
//     private var queue: [ele]
    
    
// }