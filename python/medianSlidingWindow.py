class HashHeap:
    def __init__(self, desc=False):
        self.val2idx = dict()
        self.heap = []
        self.descending = desc
    
    @property
    def size(self):
        return len(self.heap)
    
    def top(self):
        return self.heap[0] if self.heap else -1
        
    def push(self, item):
        # add to last
        self.heap.append(item)
        self.val2idx[item] = self.size - 1
        
        # siftUp with index, 
        self._sift_up(self.size - 1)
    
    def pop(self):
        item = self.heap[0]
        self.remove(item)
        return item

    def _compareSmallerWithIndex(self, left, right):
        return (
            self.heap[left] > self.heap[right] 
            if self.descending else 
            self.heap[left] < self.heap[right]
            )
        
    def remove(self, item):
        if item not in self.val2idx:
            return
        
        index = self.val2idx[item]
        # replace the empty spot with the last item in heap
        self._swap(index, self.size - 1)
        
        del self.val2idx[item]
        self.heap.pop()
        
        # make sure index don't go over bound
        # it will if the delete element is the last item
        if index < self.size:
            self._sift_up(index)
            self._sift_down(index)
    
    def _swap(self, i, j):
        item1, item2 = self.heap[i], self.heap[j]
        self.heap[i], self.heap[j] = item2, item1
        self.val2idx[item1], self.val2idx[item2] = j, i
        
    def _sift_up(self, index):
        while index != 0:
            parent = index // 2
            if self._compareSmallerWithIndex(parent, index):
                return
            self._swap(parent, index)
            index = parent # continue

    def _sift_down(self, index):
        if index is None:
            return
        # left child i index * 2, right child is index * 2 + 1
        while index * 2 < self.size:
            smallest = index
            left, right = index * 2, index * 2 + 1
            
            # right for sure smaller than left if minheap
            # so compare to left first
            if self._compareSmallerWithIndex(left, smallest):
                smallest = left
            
            if right < self.size and self._compareSmallerWithIndex(right, smallest):
                smallest = right
            
            if smallest == index:
                return
            
            self._swap(index, smallest)
            index = smallest # continue
    
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        if not nums or len(nums) < k:
            return []
            
        self.maxheap = HashHeap(desc=True)
        self.minheap = HashHeap()
        
        for i in range(0, k - 1):
            self.add((nums[i], i))
            
        medians = []
        for i in range(k - 1, len(nums)):
            self.add((nums[i], i))
            # print(self.maxheap.heap, self.median, self.minheap.heap)
            medians.append(self.median)
            self.remove((nums[i - k + 1], i - k + 1))
            # print(self.maxheap.heap, self.median, self.minheap.heap)
            
        return medians
            
    def add(self, item):
        if self.maxheap.size > self.minheap.size:
            self.minheap.push(item)
        else:
            self.maxheap.push(item)
            
        if self.maxheap.size == 0 or self.minheap.size == 0:
            return
            
        if self.maxheap.top() > self.minheap.top():
            self.maxheap.push(self.minheap.pop())
            self.minheap.push(self.maxheap.pop())
        
    def remove(self, item):
        self.maxheap.remove(item)
        self.minheap.remove(item)
        if self.maxheap.size < self.minheap.size:
            self.maxheap.push(self.minheap.pop())
        
    @property
    def median(self):
        return self.maxheap.top()[0]