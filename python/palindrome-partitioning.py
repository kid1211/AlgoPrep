class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        self.dfs(s, [], results)
        return results

    def dfs(self, s, current, results):
        if len(s) == 0:
            results.append(list(current))
            return

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if prefix != prefix[::-1]:
                continue
            current.append(prefix)
            self.dfs(s[i:], current, results)
            current.pop()
