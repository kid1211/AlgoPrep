// new -> old -> oldest
class Node<T> {
    var key: T
    var val: T
    var next: Node<T>? = nil
    var prev: Node<T>? = nil
    
    init(_ key: T, _ val: T) {
        self.val = val
        self.key = key
    }
    
    func desc() {
        print("key: \(key), value: \(val)")
    }
}

class LRUCache {
    internal var head: Node<Int>? {
        didSet {
            guard tail == nil else { return }
            tail = head
        }
    }
    internal var tail: Node<Int>?
    internal var size = 0
    internal let maxSize: Int
    
    init(_ capacity: Int) {
        maxSize = capacity
    }
    
    func get(_ key: Int) -> Int {
        guard let node = getNode(key) else { return -1 }
        return node.val
    }
    
    func put(_ key: Int, _ value: Int) {
        if var node = getNode(key) {
            node.val = value
        } else {
            addNode(key, value)
        }
    }
    
    // if no match, return nill
    internal func getNode(_ key: Int) -> Node<Int>? {
        guard var current = head else { return nil }
        
        if current.key == key {
            return current
        }
        
        // because i want to return the last one, so i should check has next, not current
        while var next = current.next {
            if next.key == key {
                removeNode(next)
                return addNode(next.key, next.val)
            }
            current = next
        }
        
        return nil
    }
    
    internal func addNode(_ key: Int, _ val: Int) -> Node<Int> {
        if size >= maxSize {
            removeNode()
        }
        
        let node = Node(key, val)
        
        // if head is not empty, update the link
        if var head = head {
            head.prev = node
            node.next = head
        }
        
        // latest is node now
        head = node
        // if tail is empty, set it, but this is handled in setter
        
        size += 1
        return node
    }
    
    internal func removeNode(_ node: Node<Int>? = nil) {
        size -= 1
        if let node = node, node.key != tail?.key {
            removeMiddle(node)
        } else {
            removeLast()
        }
    }
    
    internal func removeMiddle(_ node: Node<Int>) {
        if node.key == head?.key {
            // if there is size == 1
            head = node.next
        } else {
            // if size is more than 1
            node.prev?.next = node.next
            node.next?.prev = node.prev
        }
    }
    
    internal func removeLast() {        
        // if head and tail are equal
        if tail?.key == head?.key {
            head = nil
        }
        
        tail = tail?.prev
        tail?.next = nil
    }
    
    internal func printNodes() {
        if var current = head {
            while var next = current.next {
                current.desc()
                current = next
            }
            current.desc()
        }
        
        print("*******************")
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * let obj = LRUCache(capacity)
 * let ret_1: Int = obj.get(key)
 * obj.put(key, value)
 */

// ["LRUCache","put","put","get","put","get","put","get","get","get"]
// [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

// ["LRUCache","put","get","put","get","get"]
// [[1],[2,1],[2],[3,2],[2],[3]]

// ["LRUCache","get","put","get","put","put","get","get"]
// [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]