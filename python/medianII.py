from heapq import heappush, heappop

class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        self.maxheap, self.minheap = [], []
        
        rtn = []
        
        for num in nums:
            median = self.add(num)
            rtn.append(median)
        
        return rtn
    
    def add(self, value):
        # because of median is left align, so we want to make sure max heap is
        # either the same size or 1 bigger
        if len(self.maxheap) <= len(self.minheap):
            heappush(self.maxheap, -value)
        else:
            heappush(self.minheap, value)
        
        # make sure the maxheap head is smaller than minheap head
        if self.minheap and -self.maxheap[0] >= self.minheap[0]:
            heappush(self.maxheap, -heappop(self.minheap))
            heappush(self.minheap, -heappop(self.maxheap))
        
        return -self.maxheap[0]