class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        if s == "":
            return [[]]
        results = []
        self.dfs([], s, results)
        return results

    def dfs(self, current, s, results):
        if len(s) == 0:
            results.append(list(current))
            return

        # split string, literally, you can't
        # split in the first position cuz it never ends

        for i in range(1, len(s) + 1):
            prefix = s[:i]

            if len(prefix) > 2:
                continue

            current.append(prefix)
            self.dfs(current, s[i:], results)
            current.pop()
