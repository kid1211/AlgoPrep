class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, dict):
        # write your code here

        return True if self.dfs([], s, dict) else False

    def dfs(self, current, s, dict):
        print(current, s)
        if len(s) == 0:
            return True

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if not prefix in dict:
                continue

            current.append(prefix)
            result = self.dfs(current, s[i:], dict)
            if result:
                return True
            current.pop()
