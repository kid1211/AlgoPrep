# for the letter that didn't fit the criteria, we def won't include them in the final answer
# so the real answer will be on the left or right substring of it. just keep recursively call it then
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        count = {}

        for l in s:
            count[l] = count.get(l, 0) + 1

        for key in count.keys():
            if count[key] < k:
                return max(self.longestSubstring(subString, k) for subString in s.split(key))
        return len(s)
