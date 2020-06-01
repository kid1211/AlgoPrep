class Solution:
    """
    @param s: a string
    @return: an integer
    """

    def lengthOfLongestSubstring(self, s):
        # write your code here
        already = set()
        j, n = 0, len(s)
        longest = 0

        for i in range(n):
            while j < n and s[j] not in already:
                already.add(s[j])
                j += 1

            if s[j - 1] in already:
                longest = max(longest, j - i)

            already.remove(s[i])

        return longest
