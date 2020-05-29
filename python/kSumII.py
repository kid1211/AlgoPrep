class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """

    def kSumII(self, A, k, target):
        results = []
        self.dfs([], 0, A, k, target, results)
        return results

    def dfs(self, current, index, A, k, target, results):
        if len(current) == k:
            if sum(current) == target:
                results.append(current[:])
            return

        for i in range(index, len(A)):
            current.append(A[i])
            self.dfs(current, i + 1, A, k, target, results)
            current.pop()
