class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if len(nums) < k:
            return []

        def add(idx):
            val = (nums[idx], idx)
            if len(minheap) < len(maxheap):
                minheap.push(val)
            else:
                maxheap.push(val)

            if minheap and minheap.top < maxheap.top:
                minheap.push(maxheap.pop())
                maxheap.push(minheap.pop())

        def remove(idx):
            val = (nums[idx], idx)
            minheap.pop(val)
            maxheap.pop(val)

            if len(minheap) > len(maxheap):
                maxheap.push(minheap.pop())

        res = []
        minheap, maxheap = MinHeap(), MaxHeap()

        for i in range(k - 1):
            add(i)
        for i in range(k - 1, len(nums)):
            add(i)
            res += [
                (maxheap.top[0] + minheap.top[0]) / 2 if k % 2 == 0 else maxheap.top[0]
            ]
            remove(i - k + 1)
        return res


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

