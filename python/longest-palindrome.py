class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
        # write your code here

        # find how many pair
        findPairSet = set()
        pairs = 0

        for char in s:
            if char in findPairSet:
                findPairSet.remove(char)
                pairs += 1
            else:
                findPairSet.add(char)

        return pairs * 2 + 1 if len(findPairSet) > 0 else pairs * 2
