class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """

    def strStr(self, source, target):
        # Write your code here

        PRIME = 41
        mod = sys.maxsize // PRIME
        tgtLength, srcLength = len(target), len(source)

        if srcLength < tgtLength:
            return -1

        # target
        tgtHash, srcHash = 0, 0
        allSame = True

        for i in range(tgtLength):
            if target[i] != source[i]:
                allSame = False
            tgtHash = (tgtHash * PRIME +
                       self.getCharHash(target[i])) % mod
            srcHash = (srcHash * PRIME +
                       self.getCharHash(source[i])) % mod

        if allSame:
            return 0

        deductHash = PRIME ** (tgtLength - 1)
        for i in range(tgtLength, srcLength):
            # take out the first char
            srcHash -= self.getCharHash(source[i - tgtLength]) * deductHash
            srcHash = (srcHash + mod) % mod

            # move every char left
            srcHash *= PRIME

            # add last bit, and add mod just in case it is negative
            srcHash += self.getCharHash(source[i])

            if tgtHash == srcHash:
                start = i - tgtLength + 1
                end = i + 1

                if target == source[start:end]:
                    return start

        return -1

    def getCharHash(self, letter):
        return ord(letter) - ord('a')
