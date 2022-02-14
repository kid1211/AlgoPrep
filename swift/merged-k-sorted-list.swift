/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func mergeKLists(_ lists: [ListNode?]) -> ListNode? {
       // # heap
        var heap = HashHeap<ListNode>(true)
        
        for node in lists {
            guard let node = node else { continue }
            heap.push(node)
            
        }
        
        var dummy = ListNode()
        var curr = dummy
        while heap.top != nil {
            guard let node = heap.pop() else { continue }
            curr.next = node
            curr = node
            
            if node.next != nil {
                heap.push(node.next!)
            }
        }
        
        return dummy.next
    }
}
// https://stackoverflow.com/questions/34705786/swift-how-to-implement-hashable-protocol-based-on-object-reference
extension ListNode: Comparable, Equatable, Hashable  {
    static public func <(lhs:ListNode, rhs:ListNode) -> Bool {
        lhs.val < rhs.val
    }
    static public func ==(lhs:ListNode, rhs:ListNode) -> Bool {
        lhs === rhs
    }
    
    public func hash(into hasher: inout Hasher) {
        hasher.combine(ObjectIdentifier(self))
    }
}
   
class HashHeap<T: Hashable & Comparable> {
    private struct Node: Hashable {
        var val: T
        var identifier: Int
        init(_ val: T, _ identifier: Int = 0) {
            self.val = val
            self.identifier = identifier
        }
    }
    private var heap: [Node] = []
    private var map: [Node: Int] = [:]
    private var size: Int { heap.count }
    private let isMinHeap: Bool
    var top: T? { heap.first?.val }
    
    init(_ isMinHeap: Bool) {
        self.isMinHeap = isMinHeap
    }
    
    func push(_ val: T, _ identifier: Int = 0) { push(Node(val, identifier)) }

    func pop(_ val: T, _ identifier: Int = 0) { return pop((Node(val, identifier)))}
    
    func pop() -> T? {
        guard let top = heap.first else { return nil }
        pop(top) 
        return top.val
    }
    
    private func push(_ node: Node) {
        heap += [node]
        map[node] = size - 1
        siftUp(size - 1)
    }
    
    private func pop(_ node: Node) {
        guard let idx = map[node] else { return }
        swap(idx, size - 1)
        heap.removeLast()
        map[node] = nil
        
        if idx < size {
            siftUp(idx)
            siftDown(idx)
        }
    }
    
    private func siftUp(_ idx: Int) {
        guard idx > 0 else { return }
        let parent = (idx - 1) / 2
        guard parent != findParent([parent, idx]) else { return }
        swap(idx, parent)
        siftUp(parent)
    }
    
    private func siftDown(_ idx: Int) {
        guard idx * 2 < size else { return }
        guard 
            let parent = findParent([idx, idx * 2 + 1, idx * 2 + 2]),
            idx != parent else { return }
        swap(idx, parent)
        siftDown(parent)
    }
    
    private func swap(_ i: Int, _ j: Int) {
        (map[heap[i]], map[heap[j]]) = (j, i)
        heap.swapAt(i, j)
    }
    
    private func findParent(_ nums: [Int]) -> Int? {
        let sorted = nums.filter { $0 < heap.count }.sorted { heap[$0].val < heap[$1].val }
        return isMinHeap ? sorted.first : sorted.last
    }
}