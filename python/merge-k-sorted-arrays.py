from heapq import heappop, heappush


class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        # write your code here

        heap = []

        for i in range(len(arrays)):
            if arrays[i]:
                heappush(heap, (arrays[i][0], i, 0))

        res = []

        while heap:
            val, arrIdx, idx = heappop(heap)

            res.append(arrays[arrIdx][idx])

            nextIdx = idx + 1
            if nextIdx < len(arrays[arrIdx]):
                heappush(heap, (arrays[arrIdx][nextIdx], arrIdx, nextIdx))

        return res
