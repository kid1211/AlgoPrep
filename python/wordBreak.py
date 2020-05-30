class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, dict):
        # write your code here
        results = []
        self.dfs([], s, dict, results)
        return len(results) > 0

    def dfs(self, current, s, dict, results):
        if len(s) == 0:
            results.append(current)
            return

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if not prefix in dict:
                continue

            current.append(prefix)
            return self.dfs(current, s[i:], dict, results)
            current.pop()
