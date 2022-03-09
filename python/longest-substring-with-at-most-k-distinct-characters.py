class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res = 0
        count = collections.defaultdict(int)
        n = len(s)

        j = 0
        for i in range(n):
            while j < n and (s[j] in count or len(count) < k):
                count[s[j]] += 1
                j += 1

            if len(count) <= k:
                res = max(res, j - i)

            count[s[i]] -= 1
            if count[s[i]] <= 0:
                del count[s[i]]
        return res

