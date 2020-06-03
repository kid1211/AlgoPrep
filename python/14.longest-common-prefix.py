#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def getPrefix(str1, str2):
            if str1 != "" and str2 != "":
                n = len(str2)
                rtn = ""
                for i in range(len(str1)):
                    if i >= n or str1[i] != str2[i]:
                        return rtn
                    rtn += str1[i]
                return rtn
            else:
                return ""

        n = len(strs)
        if n == 0:
            return ""
        common = strs[0]
        for i in range(1, n):
            common = getPrefix(common, strs[i])
        return common


# @lc code=end
["dog", "racecar", "car"]
