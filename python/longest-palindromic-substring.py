class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """

    def longestPalindrome(self, s):
        # write your code here

        # insert # in-between characters in string
        newStr = "#"
        for char in s:
            newStr += char
            newStr += "#"

        testStr = "#a#b#a#a"
        # print("#: ", self.getLongestPalindrome(testStr, 0))
        # print("#a#b#a#: ", self.getLongestPalindrome(testStr, 3))
        # print("#: ", self.getLongestPalindrome(testStr, 4))
        # print('what?: ', self.getLongestPalindrome(newStr, 0))

        # for loop save the longest one
        maxLength = len(newStr)
        longest = ""
        for i in range(maxLength):
            currentLongest = self.getLongestPalindrome(newStr, i)
            if len(currentLongest) > len(longest):
                longest = currentLongest

        return longest.replace("#", "")

    """
    @parm s: input string
    @parm idx: index for the starting point
    @return: the longest palidrom start with idx
    """

    def getLongestPalindrome(self, s, idx):
        maxLength = len(s)

        def canAccess(leftIdx, rightIdx):
            return leftIdx >= 0 and rightIdx < maxLength

        leftIdx, rightIdx = idx, idx
        while s[leftIdx] == s[rightIdx]:
            if canAccess(leftIdx - 1, rightIdx + 1) == False:
                return s[leftIdx: rightIdx + 1]
            leftIdx -= 1
            rightIdx += 1

        return s[leftIdx + 1: rightIdx]
# "abaa"
# "ababaababa"
