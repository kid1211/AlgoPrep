// array
// reverse for loop
for index in stride(from: heights.count - 1, to: 0 - 1, by: -1) {}

// array reverse
res.reverse() // inplace
stack.removeLast()
stack.last != "("


// String
let temp = "hello world";
print(Array(temp))
print(String(Array(temp)))

convertedS.replacingOccurrences(of: "#", with: "")

for char in s {
    convertedS += [char]
    convertedS += ["#"]
}

convertedS.replacingOccurrences(of: "#", with: "")

func getIndex(_ i: Int) -> String.Index {
    return s.index(s.startIndex, offsetBy: i)
}


// Queue
// https://medium.com/flawless-app-stories/data-structure-in-swift-queue-part-5-985601071606


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