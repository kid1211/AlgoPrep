class HashHeap<T: Hashable & Comparable> {
    struct Node: Hashable {
        let val: T
        let identifier: Int
        
        init(_ val: T, _ identifier: Int = -1) {
            self.val = val
            self.identifier = identifier
        }
    }
    private var heap = [Node]()
    private var map = [Node:Int] ()
    var top: Node? { heap.first }
    var size: Int { heap.count }
    private let isMinHeap: Bool
    
    init(_ isMinHeap: Bool) { self.isMinHeap = isMinHeap}
    
    func push(_ node: Node) {
        heap += [node]
        map[node] = size - 1
        siftUp(size - 1)
    }
    
    func pop(_ node: Node? = nil) -> Node? {
        guard let node = node ?? heap.first else { return nil }
        guard let idx = map[node] else { return nil }
        swap(idx, size - 1)
        
        heap.removeLast()
        map[node] = nil
        
        if idx != size {
            siftUp(idx)
            siftDown(idx)
        }
        
        return node
    }
    
    private func siftUp(_ idx: Int) {
        guard idx > 0 else { return }
        let parent = (idx - 1) / 2
        if parent != findParent([idx, parent]) {
            swap(parent, idx)
            siftUp(parent)
        }
    }
    
    private func siftDown(_ idx: Int) {
        guard idx * 2 < size else { return }
        if 
            let parent = findParent([idx, idx * 2 + 1, idx * 2 + 2]),
            parent != idx {
                swap(parent, idx)
                siftDown(parent)
            }
    }
    
    private func swap(_ i: Int, _ j: Int) {
        (map[heap[i]], map[heap[j]]) = (j, i)
        heap.swapAt(i, j)
    }
    
    private func findParent(_ nums: [Int]) -> Int? {
        let sorted = nums.filter { $0 < size }.sorted { heap[$0].val < heap[$1].val }
        return isMinHeap ? sorted.first : sorted.last
    }
    
}