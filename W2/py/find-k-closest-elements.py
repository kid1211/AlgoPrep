from typing import List


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
        return []

    def testFindKClosestElement(self):
        cases = 3
        testArrys = [
            [2, 3, 4, 6, 7, 9],
            [2, 3, 6, 7, 9],
            [2, 3, 4, 4, 6, 7, 9]
        ]
        testTarget = [
            4,
            4,
            4
        ]
        expected = [
            [4, 3, 6, 2],
            [3, 2, 6, 7],
            [4, 4, 3, 2]
        ]

        for i in range(cases):
            for k in range(4):
                rtn = findKClosestElement(testArrys[i], testTarget[i], 0, k)
                print(f"TestCase {i} for {k} elements: ",
                      rtn == expected[i][:k])
        return

    def testFindClosestElement(self):
        cases = 2
        testArrys = [
            [2, 3, 4, 6, 7, 9],
            [2, 3, 6, 7, 9]
        ]
        testX = [
            4,
            4
        ]
        expected = [
            2,
            1
        ]

        for i in range(cases):
            start, end = 0, len(testArrys[i]) - 1
            rtn = self.findClosestElement(testArrys[i], testX[i], start, end)
            print(f"test cases {i}: ", expected[i] == rtn)
        return


# args = [
#     [1,2,3,4,5]
#     5,
#     2
# ]
if __name__ == '__main__':
    Solution.findClosestElements([1, 2, 3, 4, 5], 2, 2)
