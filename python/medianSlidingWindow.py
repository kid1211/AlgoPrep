class HashHeap:
    def __init__(self, desc = False):
        self.hashmap = dict()
        self.heap = []
        self.desc = desc
    
    def push(self, value):
        self.heap.append(value)
        self.hashmap[value] = self.size - 1
        
        # move it up
        self._sift_up(self.size - 1)
    
    def pop(self):
        item = self.top
        self.remove(item)
        return item
        
    def remove(self, val):
        if val not in self.hashmap:
            return
        
        # swap the last and top
        idx = self.hashmap[val]
        self._swap(idx, self.size - 1)
        
        # remove last
        del self.hashmap[val]
        self.heap.pop() # this is list pop, not heap pop
        
        if idx < self.size:
            self._sift_up(idx)
            self._sift_down(idx)
    
    @property
    def size(self):
        return len(self.heap)
    
    @property
    def top(self):
        return self.heap[0]
    
    def _sift_down(self, idx):
        while idx * 2 < self.size:
            smallest = idx
            left, right = idx * 2, idx * 2 + 1
            
            # test out if order useful
            if self._compare(left, smallest):
                smallest = left
            
            if right < self.size and self._compare(right, smallest):
                smallest = right
            
            if smallest == idx:
                return
            
            self._swap(smallest, idx)
            idx = smallest # continue
    
    def _sift_up(self, idx):
        while idx != 0:
            parent = idx // 2
            if self._compare(parent, idx):
                return
            self._swap(idx, parent)
            idx = parent

    def _swap(self, i, j):
        item1, item2 = self.heap[i], self.heap[j]
        self.heap[i], self.heap[j] = item2, item1
        self.hashmap[item1], self.hashmap[item2] = j, i
    
    def _compare(self, leftIdx, rightIdx):
        return (
            self.heap[leftIdx] < self.heap[rightIdx] if not self.desc else
            self.heap[rightIdx] < self.heap[leftIdx]
            )

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        if not nums or len(nums) < k:
            return []
            
        self.maxheap = HashHeap(desc = True)
        self.minheap = HashHeap()
        
        for i in range(k - 1):
            # adding a tuple is more unique than same value
            self.add((nums[i], i))
            
        medians = []
        for i in range(k - 1, len(nums)):
            temp = self.add((nums[i], i))
            medians.append(temp)
            self.remove((nums[i - k + 1], i - k + 1))
            
        return medians
    
    def add(self, value):
        if self.maxheap.size > self.minheap.size:
            self.minheap.push(value)
        else:
            self.maxheap.push(value)
        
        if self.minheap.size and self.maxheap.top > self.minheap.top:
            self.maxheap.push(self.minheap.pop())
            self.minheap.push(self.maxheap.pop())
        
        return self.maxheap.top[0]
    
    def remove(self, value):
        self.maxheap.remove(value)
        self.minheap.remove(value)
        
        # adjust so that it balance out
        if self.minheap.size > self.maxheap.size:
            self.maxheap.push(self.minheap.pop())