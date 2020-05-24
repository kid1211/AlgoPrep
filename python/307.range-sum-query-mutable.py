#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

# @lc code=start


class NumArray:

    def __init__(self, nums: List[int]):
        if len(nums) == 0:
            return
        self.root = self.buildTree(nums, 0, len(nums) - 1)
        # print(16)
        # self.printTree(self.root)

    def update(self, i: int, val: int) -> None:
        self.updateTree(self.root, i, val)
        # print(21)
        # self.printTree(self.root)

    def updateTree(self, root, i, val):
        if root.start == root.end == i:
            root.rangeSum = val
            return
        mid = (root.start + root.end) // 2  # floor division
        if i <= mid:
            self.updateTree(root.left, i, val)
        else:
            self.updateTree(root.right, i, val)
        root.rangeSum = root.left.rangeSum + root.right.rangeSum

    def sumRange(self, i: int, j: int) -> int:
        # print(f'sumRang: ({i},{j})')
        return self.sumRangeTree(self.root, i, j)

    def sumRangeTree(self, root, start, end):
        if root.start == start and root.end == end:
            return root.rangeSum

        mid = (root.start + root.end) // 2  # floor division
        # draw a pic, and you will know if mid == end,it will be on left side
        if mid < start:
            # on the right side
            return self.sumRangeTree(root.right, start, end)
        elif mid >= end:
            # on the left side
            return self.sumRangeTree(root.left, start, end)
        else:
            return self.sumRangeTree(root.left, start, mid) + \
                self.sumRangeTree(root.right, mid + 1, end)

    def buildTree(self, nums, start, end):
        if start == end:
            # leaf node, no left or right
            return SegmentTreeNode(start, end, nums[start])
        mid = (start + end) // 2  # floor division
        left = self.buildTree(nums, start, mid)
        right = self.buildTree(nums, mid + 1, end)
        rangeSum = left.rangeSum + right.rangeSum
        return SegmentTreeNode(start, end, rangeSum, left, right)

    def printTree(self, root):
        if root:
            self.printTree(root.left)
            leftVal = root.left.rangeSum if root.left else None
            rightVal = root.right.rangeSum if root.right else None
            print(
                f" (root: {root.rangeSum}, start:{root.start}, end: {root.end}, left: {leftVal}, right: {rightVal}) ")
            self.printTree(root.right)


class SegmentTreeNode:
    def __init__(self, start=None, end=None, rangeSum=None, left=None, right=None):
        self.start = start
        self.end = end
        self.rangeSum = rangeSum
        self.left = left
        self.right = right
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
# @lc code=end
