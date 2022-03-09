#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dfs(s, 0, p, 0, {})

    def dfs(self, s, sIdx, p, pIdx, memo):
        # print(s[sIdx:], p[pIdx:])
        if (sIdx, pIdx) in memo:
            return memo[(sIdx, pIdx)]

        if sIdx == len(s):
            for i in range(pIdx, len(p)):
                if p[i] == '*':
                    continue
                if i + 1 < len(p) and p[i + 1] == '*':
                    continue
                return False
            return True

        if pIdx == len(p):
            return False

        if pIdx + 1 < len(p) and p[pIdx + 1] == '*':
            if self.isCharMatched(s[sIdx], p[pIdx]):
                # either nothing or two
                isMatched = self.dfs(s, sIdx, p, pIdx + 2, memo) or \
                    self.dfs(s, sIdx + 1, p, pIdx, memo)
            else:
                isMatched = self.dfs(s, sIdx, p, pIdx + 2, memo)

        else:
            isMatched = self.isCharMatched(s[sIdx], p[pIdx]) and \
                self.dfs(s, sIdx + 1, p, pIdx + 1, memo)

        memo[(sIdx, pIdx)] = isMatched
        return isMatched

    def isCharMatched(self, sChar, pChar):
        return sChar == pChar or pChar == '.'


# @lc code=end
# "b"
# ""

# "bbb"
# "bb"

# "bbb"
# "bb."

# "bbb"
# "b."

# "bbb"
# "b.b"

# stage 2
# "bb"
# "c*bb"

# ""
# "b*"

# "bb"
# "b*"

# "bbb"
# "b*"

# "bbb"
# "b*b"


# true
# "ssip"
# "s*p"

# problem
# "aab"
# "c*a*b"

# # not matching
# "aab"
# "c*aab"

# problem again
# "a"
# ".*..a*"
