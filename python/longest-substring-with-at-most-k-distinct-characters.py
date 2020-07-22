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

        count = {}
        n = len(s)
        longest = 0

        j = 0
        for i in range(n):
            while j < n and (len(count) < k or s[j] in count):
                count[s[j]] = count.get(s[j], 0) + 1
                j += 1

            if len(count) >= k:
                longest = max(longest, j - i)

            # clear up
            count[s[i]] -= 1
            if count[s[i]] == 0:
                del count[s[i]]

        return longest if longest != 0 else len(s)
