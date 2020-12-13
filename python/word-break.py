class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict = set()
        for word in wordDict:
            dict.add(word)

        return self.dfs([], dict, s, {})

    def dfs(self, current, dict, s, visited):
        if len(s) == 0:
            return True

        if s in visited:
            return visited[s]

        for i in range(1, len(s) + 1):
            prefix = s[:i]

            if prefix not in dict:
                continue

            current.append(prefix)
            if self.dfs(current, dict, s[i:], visited):
                return True
            visited[s] = False
            current.pop()
