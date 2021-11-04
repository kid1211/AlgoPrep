# 19 for n == 3
# (2 * n) ^ n
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.c = 0
        return self.dfs(nums, target, 0, 0, {})

    def dfs(self, nums, target, idx, currSum, visited):
        self.c += 1
        print(self.c)
        if idx >= len(nums):
            return 1 if currSum == target else 0

        for i in range(idx, len(nums)):
            # if self.getKey(i, currSum) in visited:
            #     # print(1, currSum)
            #     continue

            count = 0
            count += self.dfs(nums, target, i + 1, currSum + nums[i], visited)
            count += self.dfs(nums, target, i + 1, currSum - nums[i], visited)

            visited[self.getKey(i, currSum)] = count

        return visited[self.getKey(idx, currSum)]

    def getKey(self, idx, currSum):
        return str(idx) + "|" + str(currSum)


# 1
# 1 1
# 1 1 1
# 1 1 -1
# 1 -1
# 1 -1 +1
# 1 -1 -1
# -1 1 1

# 27 => 3 ^ 3
# 19 for n == 3
# (2 * n) ^ n
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.count = 0
        res = []
        self.dfs([], res, nums, target, 0)
        # print(res)
        return len(res)

    def dfs(self, curr, res, nums, target, idx):
        self.count += 1
        print(self.count)
        if len(curr) >= len(nums):
            if sum(curr) == target:
                res += [list(curr)]
            return

        for i in range(idx, len(nums)):
            self.dfs(curr + [nums[i]], res, nums, target, i + 1)
            self.dfs(curr + [-nums[i]], res, nums, target, i + 1)


# 1 1
# 1 1 1
# 1 1 -1
# 1 -1
# 1 -1 +1
# 1 -1 -1
# -1 1 1

