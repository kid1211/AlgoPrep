#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dfs("", s, wordDict, {})

    def dfs(self, prefix, s, wordDict, memo):
        # print(prefix, s)
        if s in memo:
            return memo[s]
        # print(f"*{s}*")
        if s in wordDict:
            print(prefix)
            return True

        for i in range(len(s)):
            prefix = s[:i]
            # print(s[:i], s[i:])
            if prefix in wordDict:
                isWord = self.dfs(prefix, s[i:], wordDict, memo)
                memo[s] = isWord
                if isWord:
                    return True


# @lc code=end
" " "leetcode"
"leet" "code"
