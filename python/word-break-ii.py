class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]

        if s == "":
            return []

        rtn = []
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if not prefix in wordDict:
                continue
            # lint "code"
            # lint "co de"
            # all the pssible valid partition for the latter part of string
            possiblePartition = self.dfs(s[i:], wordDict, memo)
            for par in possiblePartition:
                rtn.append(prefix + " " + par)

        if s in wordDict:
            rtn.append(s)

        memo[s] = rtn
        return rtn


# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
