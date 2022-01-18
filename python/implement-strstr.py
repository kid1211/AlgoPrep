PRIME = 31
MOD = sys.maxsize // PRIME


class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """

    def strStr(self, source, target):
        # Write your code here
        n, m = len(source), len(target)
        if n < m:
            return -1

        sourceHash = 0
        targetHash = 0
        for i in range(m):
            sourceHash *= PRIME
            sourceHash += self.gethash(source[i])
            sourceHash %= MOD

            targetHash *= PRIME
            targetHash += self.gethash(target[i])
            targetHash %= MOD

        if sourceHash == targetHash:
            return 0

        co = PRIME ** (m - 1)
        for i in range(m, n):
            sourceHash -= self.gethash(source[i - m]) * co
            sourceHash *= PRIME
            sourceHash += self.gethash(source[i])

            if sourceHash == targetHash:
                return i - m + 1
        return -1

    def gethash(self, letter):
        return ord(letter) - ord("a")


class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """

    def strStr(self, source, target):
        # Write your code here
        n, m = len(source), len(target)
        if n < m:
            return -1

        for i in range(n - m + 1):
            j = 0
            while j < m and source[i + j] == target[j]:
                j += 1

            if j == m:
                return i
        return -1
