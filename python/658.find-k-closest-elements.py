#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find the closes elements first
        start, end = 0, len(arr) - 1

        # check array is 0, or 1
        if end < 0:
            return []

        if end == 0:
            return arr

        # then two pointer find the array

        closestIndexes = self.findTwoClosestElement(arr, x, start, end)
        return self.findKClosestElement(arr, x, closestIndexes[0], closestIndexes[1], k)

    # return an array for k elements
    def findKClosestElement(self, arr, target, left, right, k):
        length = len(arr)
        leftRtn = []
        rightRtn = []

        def isSafe(index):
            return index < length and index >= 0

        while isSafe(left) and isSafe(right) and (len(leftRtn) + len(rightRtn)) < k:
            leftEle, rightEle = arr[left], arr[right]

            if abs(leftEle - target) <= abs(rightEle - target):
                leftRtn.append(leftEle)
                left -= 1
            else:
                rightRtn.append(rightEle)
                right += 1

        # done all left side or all right side
        if len(leftRtn) + len(rightRtn) == k:
            return leftRtn[::-1] + rightRtn
        elif isSafe(left):
            while isSafe(left) and (len(leftRtn) + len(rightRtn)) < k:
                leftRtn.append(arr[left])
                left -= 1
        else:
            while isSafe(right) and (len(leftRtn) + len(rightRtn)) < k:
                rightRtn.append(arr[right])
                right += 1

        return leftRtn[::-1] + rightRtn

    # return index of the closes k
    def findTwoClosestElement(self, arr, target, start, end):
        if start + 1 < end:
            mid = (start + end) // 2

            if arr[mid] <= target:
                return self.findTwoClosestElement(arr, target, mid, end)
            else:
                return self.findTwoClosestElement(arr, target, start, mid)

        if abs(arr[start] - target) > abs(arr[end] - target) and (end + 1) < len(arr):
            return (end, end + 1)
        else:
            return (start, end)
# @lc code=end
