class Solution {
    func getSkyline(_ buildings: [[Int]]) -> [[Int]] {
        var tmp:[(pos:Int, height:Int, idx: Int, isStart: Bool)] = []
        for i in 0..<buildings.count {
            let start = buildings[i][0]
            let end = buildings[i][1]
            let height = buildings[i][2]
            
            tmp += [(start, height, i, true)]
            tmp += [(end, height, i, false)]
        }
        
        var maxHeap = HashHeap<Int>(false)
        var intervals:[(start: Int, end: Int, height: Int)] = []
        var lastPos: Int?
        
        func merge(_ start: Int?, _ end: Int, _ height: Int) {
            guard let start = start, start != end && height != 0 else { return }
            
            if let last = intervals.last, last.end == start && last.height == height {
                intervals[intervals.count - 1] = (last.start, end, height)
                return
            }
            
            intervals += [(start, end, height)]
        }
        
        for (pos, height, idx, isStart) in tmp.sorted { ($0.pos, $0.height, $0.idx) < ($1.pos, $1.height, $1.idx) } {
            merge(lastPos, pos, maxHeap.top ?? 0)
            lastPos = pos
            
            isStart ? maxHeap.push(height, idx) : maxHeap.pop(height, idx)
        }
        
        var res: [[Int]] = []
        
        for (start, end, height) in intervals {
            if let last = res.last, last[0] == start && last[1] == 0 {
                res.removeLast()
            }
            
            res += [[start, height]]
            res += [[end, 0]]
        }
        
        return res
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