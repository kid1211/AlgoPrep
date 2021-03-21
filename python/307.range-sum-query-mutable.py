class NumArray:
    def __init__(self, nums: List[int]):
        if not nums:
            return None
        self.root = self.buildTree(nums, 0, len(nums) - 1)
        printTree(self.root)

    def update(self, i: int, val: int) -> None:
        def updateDFS(node, i, val):
            if not node:
                return None

            if node.start == node.end == i:
                node.sums = val
                return

            mid = (node.start + node.end) // 2

            if i <= mid:
                updateDFS(node.left, i, val)
            else:
                updateDFS(node.right, i, val)

            node.sums = node.left.sums + node.right.sums

        updateDFS(self.root, i, val)

    def sumRange(self, i: int, j: int) -> int:
        def sumRange(node, i, j):
            if node.start == i and node.end == j:
                return node.sums

            if j < i:
                return -1

            mid = (node.start + node.end) // 2

            if j <= mid:
                return sumRange(node.left, i, j)
            elif i > mid:
                return sumRange(node.right, i, j)
            else:
                return sumRange(node.left, i, mid) + sumRange(node.right, mid + 1, j)

        return sumRange(self.root, i, j)

    def buildTree(self, nums, start, end):
        if start == end:
            return SegmentalTreeNode(start, start, nums[start])

        mid = (start + end) // 2
        left = self.buildTree(nums, start, mid)
        right = self.buildTree(nums, mid + 1, end)

        return SegmentalTreeNode(start, end, left.sums + right.sums, left, right)


def printTree(root):
    if not root:
        return

    printTree(root.left)
    print(root.start, root.end, root.sums)
    printTree(root.right)


class SegmentalTreeNode:
    def __init__(self, start, end, sums, left=None, right=None):
        self.start = start
        self.end = end
        self.sums = sums
        self.left = left
        self.right = right


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)