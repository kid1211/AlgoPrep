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


class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """

    def medianII(self, nums):
        # write your code here
        if not nums:
            return []
        self.minheap = []
        self.maxheap = [-nums[0]]

        res = [nums[0]]
        for i in range(1, len(nums)):
            self.add(nums[i])
            # print(self.maxheap, self.minheap)
            res += [-self.maxheap[0]]
        return res

    def add(self, val):
        if val < -self.maxheap[0]:
            heappush(self.maxheap, -val)
        else:
            heappush(self.minheap, val)

        # we alwasy want maxheap the same size as min heap or 1 bigger
        if len(self.maxheap) - 1 > len(self.minheap):
            heappush(self.minheap, -heappop(self.maxheap))

        if len(self.minheap) > len(self.maxheap):
            heappush(self.maxheap, -heappop(self.minheap))
