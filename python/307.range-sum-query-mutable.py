class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return
        self.root = self.buildTree(nums, 0, len(nums) - 1)

    def update(self, i: int, val: int) -> None:
        self.updateDFS(self.root, i, val)

    def updateDFS(self, node, i, val):
        if not node:
            return

        start, end = node.start, node.end
        if start == end == i:
            node.sums = val
            return

        mid = (start + end) // 2

        if i <= mid:
            self.updateDFS(node.left, i, val)
        else:
            self.updateDFS(node.right, i, val)

        node.sums = node.left.sums + node.right.sums

    def sumRange(self, i: int, j: int) -> int:
        return self.sumRangeDFS(i, j, self.root)

    def sumRangeDFS(self, i, j, node):
        start, end = node.start, node.end
        if start == i and end == j:
            return node.sums

        mid = (start + end) // 2
        # check i and j both align on oneside
        # noted that mid is grounded it,  so i need to atleast
        # greater than start, think of i,j = 2, 3
        if j <= mid:
            return self.sumRangeDFS(i, j, node.left)
        elif i > mid:
            return self.sumRangeDFS(i, j, node.right)
        else:
            return self.sumRangeDFS(i, mid, node.left) + self.sumRangeDFS(mid + 1, j, node.right)

    def buildTree(self, nums, start, end):
        if start == end:
            return SegmentalTreeNode(start, end, nums[start])

        mid = (start + end) // 2
        left = self.buildTree(nums, start, mid)
        right = self.buildTree(nums, mid + 1, end)
        return SegmentalTreeNode(start, end, left.sums + right.sums, left, right)

    def printTree(self, node):
        if not node:
            return

        self.printTree(node.left)
        print(node)
        self.printTree(node.right)


class SegmentalTreeNode:
    def __init__(self, start, end, sums, left=None, right=None):
        self.start = start
        self.end = end
        self.sums = sums
        self.left = left
        self.right = right

    def __repr__(self):
        if self is None:
            return "Node is None"
        return f"<Node start:{self.start} end:{self.end} sums:{self.sums}>"


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
