class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s):
        # write your code here
        sanitized = "".join(e.lower() for e in s if e.isalnum())

        maxLength = len(sanitized)
        leftIdx = 0
        rightIdx = maxLength - 1

        if leftIdx >= rightIdx:
            return True

        while leftIdx < rightIdx and sanitized[leftIdx] == sanitized[rightIdx]:
            leftIdx += 1
            rightIdx -= 1

        return sanitized[leftIdx] == sanitized[rightIdx]
