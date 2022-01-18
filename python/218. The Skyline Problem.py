class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        tmp = []

        for i in range(len(buildings)):
            start, end, height = buildings[i]
            tmp += [(start, height, i, True)]
            tmp += [(end, height, i, False)]

        maxheap = MaxHeap()
        intervals = []
        lastpos = None
        for pos, height, index, isStart in sorted(tmp):
            maxHeight = maxheap.top[0] if len(maxheap) else 0
            self.mergeTo(intervals, lastpos, pos, maxHeight)
            if isStart:
                maxheap.push((height, index))
            else:
                maxheap.pop((height, index))
            lastpos = pos

        res = []
        for start, end, height in intervals:
            if res and res[-1][0] == start:
                res.pop()
            res += [[start, height]]
            res += [[end, 0]]
        # print(intervals)
        return res

    # lint code
    def mergeTo(self, intervals, start, end, height):
        if start is None or height == 0 or start == end:
            return
        if not intervals:
            intervals.append([start, end, height])
            return
        _, prevEnd, prevHeight = intervals[-1]
        if prevHeight == height and prevEnd == start:
            intervals[-1][1] = end
            return
        intervals.append([start, end, height])


class HashHeap:
    def __init__(self):
        self.heap = []
        self.map = {}

    def __len__(self):
        return len(self.heap)

    @property
    def top(self):
        return self.heap[0]

    @property
    def last(self):
        return len(self) - 1

    def push(self, val):
        self.heap += [val]
        self.map[val] = self.last
        self._siftup(self.last)

    def pop(self, val=None):
        if not val:
            val = self.top
        if val not in self.map:
            return

        # move to last
        idx = self.map[val]
        self._swap(idx, self.last)

        # then pop
        del self.map[val]
        self.heap.pop()

        if idx != len(self):
            self._siftup(idx)
            self._siftdown(idx)

        return val

    def _swap(self, i, j):
        tmp1, tmp2 = self.heap[i], self.heap[j]
        self.heap[i], self.heap[j] = tmp2, tmp1
        self.map[tmp1], self.map[tmp2] = j, i

    def _siftup(self, idx):
        while idx != 0:
            parent = (idx - 1) // 2
            if parent == self._findParent([parent, idx]):
                return
            self._swap(parent, idx)
            idx = parent

    def _siftdown(self, idx):
        while idx * 2 < len(self):
            left, right = idx * 2 + 1, idx * 2 + 2
            parent = self._findParent([left, right, idx])
            if idx == parent:
                return
            self._swap(parent, idx)
            idx = parent


class MinHeap(HashHeap):
    def _findParent(self, canadiates):
        return min(
            canadiates, key=lambda i: self.heap[i][0] if i < len(self) else sys.maxsize
        )


class MaxHeap(HashHeap):
    def _findParent(self, canadiates):
        return max(
            canadiates, key=lambda i: self.heap[i][0] if i < len(self) else -sys.maxsize
        )

