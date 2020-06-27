class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0
        start, end = 1, max(L)

        while start + 1 < end:
            mid = (start + end) // 2
            if self.cutIntoPieces(L, mid) >= k:
                start = mid
            else:
                end = mid

        if self.cutIntoPieces(L, end) >= k:
            return end
        elif self.cutIntoPieces(L, start) >= k:
            return start
        else:
            return 0

    def cutIntoPieces(self, L, length):
        pieces = 0

        for num in L:
            # turn the while loop to this
            pieces += (num // length)
        return pieces