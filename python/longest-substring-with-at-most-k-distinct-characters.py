class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if k == 0:
            return 0

        longest, n = 0, len(s)
        unique = {}

        j = 0
        for i in range(n):
            while j < n and (len(unique) < k or s[j] in unique):
                if s[j] not in unique:
                    unique[s[j]] = 1
                else:
                    unique[s[j]] += 1
                j += 1

            if len(unique) == k:
                longest = max(longest, j - i)

            if unique[s[i]] == 1:
                del unique[s[i]]
            else:
                unique[s[i]] -= 1

        return longest if longest != 0 else len(s)
