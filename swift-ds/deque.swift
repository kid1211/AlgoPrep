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

    var firstVal: T? { first?.val }
    var lastVal: T? { last?.val }
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
            node.prev = last
            last = node
        }
    }
    
    func removeFirst() -> T? {
        guard let tmp = first else { return nil }
        first = tmp.next
        
        if first == nil {
            last = nil
        } else {
           first!.prev = nil 
        }
        
        return tmp.val
    }
    
    func removeLast() -> T? {
        guard let tmp = last else { return nil }
        last = tmp.prev
        
        if last == nil {
            first = nil
        } else {
            last!.next = nil
        }
        
        return tmp.val
    }  
}