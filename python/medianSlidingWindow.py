class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        if not nums or len(nums) < k:
            return []
            
        maxheap, minheap = MaxHeap(), MinHeap()
        res = []
        
        def getMedian():
            return (maxheap.top[0] +  minheap.top[0]) / 2 if k % 2 == 0 else maxheap.top[0]
            
        def add(idx):
            value = (nums[idx], idx)
            if len(maxheap) > len(minheap):
                minheap.push(value)
            else:
                maxheap.push(value)
            
            if len(minheap) and maxheap.top > minheap.top:
                maxheap.push(minheap.pop())
                minheap.push(maxheap.pop())
        
        def remove(idx):
            value = (nums[idx], idx)
            maxheap.pop(value)
            minheap.pop(value)
            
            # maxHeap always need to be the same or 1 bigger
            if len(minheap) > len(maxheap):
                maxheap.push(minheap.pop())
        
        for i in range(k - 1): add(i)
            
        for i in range(k - 1, len(nums)):
            add(i)
            res += [getMedian()]
            remove(i - k + 1)
            
        return res

class HashHeap:
    def __init__(self):
        self.hashmap = {}
        self.heap = []
    
    def push(self, value):
        self.heap += [value]
        self.hashmap[value] = len(self) - 1
        
        # move it up
        self._sift_up(len(self) - 1)
        
    def pop(self, val=None):
        if not val:
            val = self.top
            
        if val not in self.hashmap:
            return None
        
        # swap the last and top
        idx = self.hashmap[val]
        self._swap(idx, len(self) - 1)
        
        # remove last
        del self.hashmap[val]
        self.heap.pop() # this is list pop, not heap pop
        
        if idx != len(self):
            self._sift_up(idx)
            self._sift_down(idx)
        return val
    
    def __len__(self):
        return len(self.heap)
    
    @property
    def top(self):
        return self.heap[0]
    
    def _sift_down(self, idx):
        while idx * 2 < len(self):
            left, right = idx * 2, idx * 2 + 1
            parent = self._getParent([left, right, idx])
            if parent == idx:
                return
            
            self._swap(parent, idx)
            idx = parent
    
    def _sift_up(self, idx):
        while idx != 0:
            parent = idx // 2
            if parent == self._getParent([parent, idx]):
                return
            
            self._swap(idx, parent)
            idx = parent

    def _swap(self, i, j):
        item1, item2 = self.heap[i], self.heap[j]
        self.heap[i], self.heap[j] = item2, item1
        self.hashmap[item1], self.hashmap[item2] = j, i

    def _getVal(self, idx, default):
        return self.heap[idx] if idx < len(self) else (default, None)

class MinHeap(HashHeap):
    def _getParent(self, canadiates):
        return min(canadiates, key = lambda k: self._getVal(k, sys.maxsize))

class MaxHeap(HashHeap):
    def _getParent(self, canadiates):
        return max(canadiates, key = lambda k: self._getVal(k, - sys.maxsize))