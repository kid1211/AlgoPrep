import heapq


class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """

    def topk(self, nums, k):
        # write your code here
        # heap = heapq.heapify(nums)

        # for num in nums:
        #     heapq.heappush(heap, num)

        # results = []
        # for _ in range(k):
        #     results.append(heapq.heappop(heap))

        return heapq.nlargest(k, nums)
