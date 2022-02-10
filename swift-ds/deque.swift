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

    private var first: Node<T>?
    private var last: Node<T>?
    var hasValue: Bool { first != nil }
    
    init() {}
    
    func append(_ val: T) {
        var node = Node(val)
        
        if first == nil {
            first = node
            last = first
        } else {
            last!.next = node
            last = node
        }
    }
    
    static func += (lhs: inout Deque<T>, rhs: T) {
        lhs.append(rhs)
    }
    
    func removeFirst() -> T? {
        guard let tmp = first else { return nil }
        first = first!.next
        return tmp.val
    }
    
    func removeLast() -> T? {
        guard let tmp = last else { return nil }
        last = last!.next
        return tmp.val
    }  
}