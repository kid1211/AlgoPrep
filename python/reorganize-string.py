import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return ""

        unique = {}

        for l in S:
            unique[l] = unique.get(l, 0) + 1

        heap = []
        for key in unique.keys():
            heapq.heappush(heap, (-unique[key], key))

        res = ""
        if -heap[0][0] > (len(S) // 2) + 1:
            return res

        while heap:
            occurence, char = heapq.heappop(heap)
            if not res or res[-1] != char:
                res += char
                if -occurence <= 1:
                    continue
                else:
                    heapq.heappush(heap, (occurence + 1, char))
            elif not heap:
                return ""
            else:
                secondOccurence, secondChar = heapq.heappop(heap)

                res += secondChar
                if -secondOccurence > 1:
                    heapq.heappush(heap, (secondOccurence + 1, secondChar))
                heapq.heappush(heap, (occurence, char))

        return res
