#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        return self.dfs(s, 0, p, 0, {})

    def dfs(self, s, sIdx, p, pIdx, memo):
        if (sIdx, pIdx) in memo:
            return memo[(sIdx, pIdx)]

        # print(s[sIdx:], p[pIdx:])
        if len(s) == sIdx:
            for i in range(pIdx, len(p)):
                if p[i] != '*':
                    return False
            return True

        if len(p) == pIdx:
            return False

        if p[pIdx] == '*':
            # abab vs *a
            # 1. match nothing: abab vs a
            # 2. match more than 1: bab vs *a
            # 3. match one: bab vs a  but this will be covered by 2 Genius!

            isMatched = self.dfs(s, sIdx + 1, p, pIdx, memo) or  \
                self.dfs(s, sIdx, p, pIdx + 1, memo)
        else:
            isMatched = self.isCharMatched(
                s[sIdx], p[pIdx]) and self.dfs(s, sIdx + 1, p, pIdx + 1, memo)

        memo[(sIdx, pIdx)] = isMatched
        return isMatched

    def isCharMatched(self, sLetter, pLetter):
        return sLetter == pLetter or pLetter == '?'

# @lc code=end
# if start with * loop through
# one to one until s finished, then check if the rest are * in p


# "abefcdgiescdfimde"
# "ab*cd?i*de"

# abab
# *a*b

# .*
