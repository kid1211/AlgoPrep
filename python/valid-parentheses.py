class Solution:
    def isValid(self, s: str) -> bool:
        # mono stack sorta
        pair = {"(": ")", "{": "}", "[": "]"}

        stack = []
        for c in s:
            if c in pair:
                stack.append(c)
                continue

            if not stack or not pair[stack.pop()] == c:
                return False

        return not stack
