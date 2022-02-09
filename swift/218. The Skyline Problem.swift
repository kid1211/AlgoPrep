// Change recurisve, and consdier simplife the tupid min/max
struct Point: Comparable {
    let pos: Int
    let height: Int
    let idx: Int
    let isStart: Bool
    
    init(_ pos: Int, _ height: Int, _ idx: Int, _ isStart: Bool) {
        self.pos = pos
        self.height = height
        self.idx = idx
        self.isStart = isStart
    }
    
    static func < (lhs: Point, rhs: Point) -> Bool {
        guard lhs.pos == rhs.pos else { return lhs.pos < rhs.pos }
        guard lhs.height == rhs.height else { return lhs.height < rhs.height }
        return (lhs.isStart, rhs.isStart) == (false, true) ? false : true
    }
}
// [[2, 3, 10], [3, 7, 15]] 5 7 15
// [[2, 3, 10], [3, 7, 15], [7, 12, 12]] 9 12 12
// [[2, 3, 10], [3, 7, 15], [7, 12, 12], [15, 20, 10]] 19 20 10
// [[2, 3, 10], [3, 7, 15], [7, 12, 12], [15, 20, 10], [20, 24, 8]]

class Solution {
    func getSkyline(_ buildings: [[Int]]) -> [[Int]] {
        
        var tmp : [Point] = []
        for i in 0..<buildings.count {
            let start = buildings[i][0], end = buildings[i][1], height = buildings[i][2]
            tmp += [Point(start, height, i, true)] // i to diferentiated
            tmp += [Point(end, height, i, false)]
        }
        
        var maxHeap = HashHeap<Int>(false)
        var intervals: [(start: Int, end: Int, height: Int)] = []
        var lastPos: Int?
        
        func mergeTo(_ start: Int?, _ end: Int, _ height:Int) {
            guard let start = start, start != end && height != 0 else { return }
            
            if let last = intervals.last, last.height == height && last.end == start {
                intervals[intervals.count - 1] = (last.start, end, height)
            } else {
                intervals += [(start, end, height)]
            }
        }

        for pt in tmp.sorted()  {
            let maxHeight = maxHeap.top?.val ?? 0
            mergeTo(lastPos, pt.pos, maxHeight)
            lastPos = pt.pos
            
            let node = HashHeap.Node(pt.height, pt.idx)
            pt.isStart ? maxHeap.push(node) : maxHeap.pop(node)
        }
        
        var res: [[Int]] = []
        
        for (start, end, height) in intervals {
            if let last = res.last, last[0] == start, last[1] == 0 {
                // remove the unncessary (end, 0), because now that start is there, it wont' be 0
                res.removeLast()
            }
            res += [[start, height]]
            res += [[end, 0]]
        }
        // print(intervals)
        return res
    }
}

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

