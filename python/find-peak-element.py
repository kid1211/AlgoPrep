class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here\
        start, end = 0, len(A) - 1
        while start <= end:
            mid = (start + end) // 2
            if A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid + 1] < A[mid]:
                end = mid - 1
            else:
                start = mid + 1
        
        return start if A[start] > A[end] else end
        