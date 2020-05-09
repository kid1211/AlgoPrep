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
        # all other cases, we need to sort based on the closes env

        # test first module
        # self.testFindClosestElement()
        self.testFindKClosestElement()

        # then two pointer find the array

        return []

    # return index of the closes k
    def findClosestElement(self, arr, target, start, end):
        if start + 1 < end:
            mid = (start + end) // 2

            if arr[mid] <= target:
                return self.findClosestElement(arr, target, mid, end)
            else:
                return self.findClosestElement(arr, target, start, mid)

        if abs(arr[start] - target) <= abs(arr[end] - target):
            return start
        else:
            return end
    # return an array for k elements

    def findKClosestElement(self, arr, target, index, k):
        length = len(arr)

        def isSafe(index):
            return index < length and index >= 0

        left, right = 0, 0
        if isSafe(index + 1):
            left, right = index, index + 1
        elif isSafe(index - 1):
            left, right = index - 1, index
        else:
            return []

        def getNextLR(left, right, isLeft):
            if isLeft:
                if isSafe(left - 1):
                    return (left - 1, right)
                elif isSafe(right + 1):
                    return (left, right + 1)
            else:
                if isSafe(right + 1):
                    return (left, right + 1)
                elif isSafe(left - 1):
                    return (left - 1, right)

            return (-1, -1)
        rtn = []
        while len(rtn) < k:
            leftEle, rightEle = arr[left], arr[right]
            if abs(leftEle - target) == abs(rightEle - target):
                if leftEle < rightEle:
                    rtn.append(leftEle)
                    left, right = getNextLR(left, right, True)
                    if left == -1:
                        return rtn
                else:
                    rtn.append(rightEle)
                    left, right = getNextLR(left, right, False)
                    if left == -1:
                        return rtn
            elif abs(leftEle - target) < abs(rightEle - target):
                rtn.append(leftEle)
                left, right = getNextLR(left, right, True)
                if left == -1:
                    return rtn
            else:
                rtn.append(rightEle)
                left, right = getNextLR(left, right, False)
                if left == -1:
                    return rtn

        return rtn

    def testFindKClosestElement(self):
        cases = 3
        testArrys = [
            [2, 3, 4, 6, 7, 9],
            [2, 3, 6, 7, 9],
            [2, 3, 4, 4, 6, 7, 9]
        ]
        expected = [
            [4, 3, 2, 6],
            [3, 2, 6, 7],
            [4, 4, 3, 2]
        ]

        for i in range(cases):
            for k in range(4):
                if i != 1 or k != 3:
                    continue

                currArry = testArrys[i]
                # print(currArry, currTarget)

                start, end = 0, len(currArry) - 1

                closestIndex = self.findClosestElement(
                    currArry, 4, start, end)
                print(f"closestIndex: {closestIndex}")
                rtn = self.findKClosestElement(
                    currArry, 4, closestIndex, k)

                print(rtn)
                print(expected[i][:k])
                print(
                    f"TestCase {i} for {k} elements: {rtn == expected[i][:k]}")
        return

    def testFindClosestElement(self):
        cases = 2
        testArrys = [
            [2, 3, 4, 6, 7, 9],
            [2, 3, 6, 7, 9]
        ]
        expected = [
            2,
            1
        ]

        for i in range(cases):
            start, end = 0, len(testArrys[i]) - 1
            rtn = self.findClosestElement(testArrys[i], 4, start, end)
            print(f"test cases {i}: ", expected[i] == rtn)
        return

# @lc code=end
