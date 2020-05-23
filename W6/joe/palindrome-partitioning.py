class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """

    def partition(self, s):
        # write your code here
        results = []
        self.dfs([], s, results)
        return results

    def dfs(self, current, s, results):
        if len(s) == 0:
            results.append(list(current))

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if not self.isValid(prefix):
                continue
            current.append(prefix)
            self.dfs(current, s[i:], results)
            current.pop()

    def isValid(self, text):
        return text == text[::-1]
