class Solution {
    
    func canFinish(_ numCourses: Int, _ prerequisites: [[Int]]) -> Bool {
        var (indegree, maps) = getMapAndEntryPoint(numCourses, prerequisites)
        var queue = Queue<Int>();
        
        for (key, value) in indegree where value == 0 {
            queue.enqueue(key)
        }
        
        // print(queue.description)
        var seq = [Int]()
        while !queue.isEmpty {
            guard var course = queue.dequeue() else { continue }
            seq += [course]
            
            for availableCourse in maps[course]! {
                indegree[availableCourse]? -= 1
                
                if indegree[availableCourse] == 0 {
                    queue.enqueue(availableCourse)
                }
            }
        }
        
        return seq.count == numCourses
    }
    
    func getMapAndEntryPoint(_ numCourses: Int, _ prerequisites: [[Int]])-> ([Int: Int], [Int: [Int]]) {
        var indegree = [Int: Int]()
        var maps = [Int: [Int]]()
        
        // init indegree
        for num in 0..<numCourses {
            indegree[num] = 0
            maps[num] = []
        }
        
        for item in prerequisites {
            let course = item[0];
            let preq = item[1];
            
            maps[preq]?.append(course)
            indegree[course]? += 1
        }
        
        return (indegree, maps)   
    }
}

struct Queue<T>: CustomStringConvertible {
    private var elements: [T] = []
    public init() {}
    
    // public init(_ array:[T]) { 
    //     array.forEach { enqueue($0) }
    // }
    
    var isEmpty: Bool {
        elements.isEmpty
    }
    
    var peek: T? {
        elements.first
    }
    
    var description: String {
        if isEmpty { return "Queue is empty ..."}
        return "---- Queue start ---\n"
            + elements.map({"\($0)"}).joined(separator: " -> ")
            + "\n --- Queue End ---"
    }
    
    mutating func enqueue(_ value: T) {
        elements.append(value)
    }
    
    mutating func dequeue() -> T? {
        isEmpty ? nil : elements.removeFirst()
    }
}