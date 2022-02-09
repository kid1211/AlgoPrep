class HashHeap<T: Comparable & Hashable> {
    struct Node: Hashable {
        let val:T
        let idx: Int
        
        init(_ val: T, _ idx: Int) {
            self.val = val
            self.idx = idx
        }
    }
    
    private let isMinHeap: Bool
    private var heap: [Node] = []
    private var map: [Node: Int] = [:]    
    
    var top: Node? { heap.first }
    private var size: Int { heap.count }
    
    init(_ isMinHeap: Bool) {
        self.isMinHeap = isMinHeap
    }
    
    func push(_ node: Node) {
        heap += [node]
        map[node] = size - 1
        siftup(size - 1)
    }
    
    func pop(_ node: Node?){
        let node = node == nil ? top : node
        guard let idx = map[node!] else { return }
        swap(idx, size - 1)
        
        map[node!] = nil
        heap.removeLast()
        
        if idx != size {
            siftup(idx)
            siftdown(idx)
        }
        
    }
    private func siftup(_ idx: Int) {
        guard idx != 0 else { return }
        let parent = (idx - 1) / 2
        guard parent != findParent([parent, idx]) else { return }
        swap(parent, idx)
        siftup(parent)

    }
    
    private func siftdown(_ idx: Int) {
        guard idx * 2 < size else { return }
        guard 
            let parent = findParent([idx, idx * 2 + 1, idx * 2 + 2]),
            parent != idx else { return }
        swap(parent, idx)
        siftdown(parent)
    }
    
    private func swap(_ i: Int, _ j: Int) {
        (map[heap[i]], map[heap[j]]) = (j, i)
        heap.swapAt(i, j)
    }
    
    private func findParent(_ candidates: [Int]) -> Int? {
        let sorted = candidates.filter{ 
            $0 < heap.count 
        }.sorted {
            heap[$0].val <= heap[$1].val
        }
        return isMinHeap ? sorted.first : sorted.last
    }
}