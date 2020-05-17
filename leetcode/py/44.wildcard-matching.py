#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pIdx = 0
        while pIdx < len(p) and p[pIdx] == '*':
            pIdx += 1

        return self.dfs(s, 0, p, pIdx)

    def dfs(self, s, sIdx, p, pIdx):
        if len(s) == sIdx:
            for i in range(pIdx, len(p)):
                if p[i] != '*':
                    return False
            return True

        # actual dfs
        for i in range(sIdx, len(s)):
            if p[pIdx] == '*':
                self.dfs(s, i + 1, p, pIdx)
                self.dfs(s, i + 1, p, pIdx + 1)
            elif self.isCharMatched():
                pass

                pass

    def isCharMatched(self, sLetter, pLetter)

            pass

        pass

# @lc code=end
# if start with * loop through
# one to one until s finished, then check if the rest are * in p
