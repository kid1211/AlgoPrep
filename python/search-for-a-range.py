class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]

        if len(A) == 1:
            return [0, 0] if A[0] == target else [-1, -1]

        return [binarySearchLast(A, target, True), binarySearchLast(A, target, False)]


def binarySearchLast(A, target, getFirst):
    left, right = 0, len(A) - 1

    while left <= right:
        mid = (left + right) // 2

        if isMatchingTarget(A[mid], target, getFirst):
            left = mid + 1
        else:
            right = mid - 1

    if getFirst:
        return left if left < len(A) and A[left] == target else -1
    else:
        return right if right >= 0 and A[right] == target else -1


def isMatchingTarget(midVal, target, getFirst):
    return midVal < target if getFirst else midVal <= target
