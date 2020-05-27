#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        self.dfs([], n, n, results)
        return results
    # index is how many open bracket

    def dfs(self, current, openBracket, closeBracket, results):
        # remainder of the open/close bracket
        if openBracket > closeBracket:
            return

        if openBracket == 0 and closeBracket == 0:
            results.append("".join(current))
        if openBracket > 0:
            current.append("(")
            self.dfs(current, openBracket - 1, closeBracket, results)
            current.pop()
        if closeBracket > 0:
            current.append(")")
            self.dfs(current, openBracket, closeBracket - 1, results)
            current.pop()


# @lc code=end
(())
()()
