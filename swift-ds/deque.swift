class Deque<T> {
    private class Node<T> {
        var val: T
        var prev: Node?
        var next: Node?
        
        init(_ val: T, _ prev: Node? = nil, _ next: Node? = nil) {
            self.val = val
            self.prev = prev
            self.next = next
        }
    }

    var first: T? { firstNode?.val }
    var last: T? { lastNode?.val }
    private var firstNode: Node<T>?
    private var lastNode: Node<T>?
    var count = 0 {
        didSet {
            if count == 0 {
                firstNode = nil
                lastNode = nil
            }
        }
    }
    var isEmpty: Bool { count <= 0 }
    
    init() {}
    init(_ array: [T]) { self += array }
    
    func append(_ val: T) {
        var node = Node(val)
        count += 1
        ``
        if let lastN = lastNode {
            lastN.next = node
            node.prev = lastNode
        } else {
            firstNode = node
        }
        
        lastNode = node
    }
    
    func removeFirst() -> T {
        let res = firstNode!.val
        firstNode = firstNode?.next
        count -= 1
        firstNode?.prev = nil 
        return res
    }
    
    func removeLast() -> T {
        let res = lastNode!.val
        lastNode = lastNode?.prev
        count -= 1
        lastNode?.next = nil
        return res
    }
    
    public static func += (lhs: Deque<T>, rhs: [T]) {
        rhs.forEach { lhs.append($0) }
    }
}