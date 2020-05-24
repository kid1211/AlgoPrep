#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
LETTER_MAPPING = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz"
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        results = []
        self.dfs([], 0, results, digits)
        return results

    def dfs(self, current, index, results, digits):
        # print(current)
        length = len(digits)
        currentLength = len(current)
        if currentLength == length and currentLength > 0:
            results.append("".join(current))
            return

        for i in range(index, length):
            letters = LETTER_MAPPING[digits[i]]
            for l in range(len(letters)):
                current.append(letters[l])
                self.dfs(current, i + 1, results, digits)
                current.pop()


# @lc code=end
