class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # write your code here
        left = self.binarySearchFirstPosition(A, target)
        if left == -1:
            return [-1, -1]
        right = self.binarySearchLastPosition(A, target)

        return [left, right]

    def binarySearchFirstPosition(self, A, target):
        left, right = 0, len(A) - 1

        while left <= right:
            mid = (left + right) // 2
            if A[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        if 0 <= left < len(A) and A[left] == target:
            return left
        else:
            return -1

    def binarySearchLastPosition(self, A, target):
        left, right = 0, len(A) - 1

        while left <= right:
            mid = (left + right) // 2
            if A[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right if A[right] == target else -1
