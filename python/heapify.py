class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """

    def heapify(self, A):
        # go through all the subtree notes
        for i in range(len(A) // 2, -1, -1):
            self.siftdown(A, i)

    def siftdown(self, A, k):
        # left child and right child
        # [i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i]
        rootLeftRight = [k, k * 2 + 1, k * 2 + 2]

        minIdx = min(
            rootLeftRight,
            key=lambda i: A[i] if i < len(A) else sys.maxsize
        )

        if k != minIdx:
            A[minIdx], A[k] = A[k], A[minIdx]
            self.siftdown(A, minIdx)
