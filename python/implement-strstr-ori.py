class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """

    def strStr(self, source, target):
        # Write your code here

        self.PRIME = 26
        self.mod = 45  # sys.maxsize / self.PRIME
        tgtLength = len(target)
        srcLength = len(source)

        if srcLength < tgtLength:
            return -1

        # target
        tgtHash = self.getStrHash(target, tgtLength)
        srcHash = self.getStrHash(source, tgtLength)
        deductHash = self.PRIME ** (tgtLength - 1)
        # print(deductHash == 26 **5)

        if tgtHash == srcHash and target == source[0: 0 + tgtLength]:
            return 0

        # test = hashValue
        # expected = (self.getCharHash('t')*26**5 + self.getCharHash('a')*26**4 + self.getCharHash('r')*26**3 + self.getCharHash('g')*26**2 + self.getCharHash('e')*26**1 + self.getCharHash('t')*26**0) %self. mod
        # print(tgtHash == expected)
        # print(source[1: 1+tgtLength])

        def modSrcStr():
            return (srcHash + self.mod) % self.mod

        for i in range(tgtLength, srcLength):
            # take out the first char
            srcHash -= self.getCharHash(source[i - tgtLength]) * deductHash
            srcHash = modSrcStr()
            # expect = (self.getCharHash('a')*26**4 + self.getCharHash('r')*26**3 + self.getCharHash('g')*26**2 + self.getCharHash('e')*26**1 + self.getCharHash('t')*26**0) % self. mod
            # print(srcHash, expect)

            # move every char left
            srcHash *= self.PRIME

            # add last bit, and add mod just in case it is negative
            srcHash += self.getCharHash(source[i])
            srcHash = modSrcStr()
            # print(srcHash == tgtHash)
            # print(source[i - tgtLength : i])

            if tgtHash == srcHash:
                start = i - tgtLength + 1
                end = i + 1

                if target == source[start:end]:
                    return start

        return -1

    def getCharHash(self, letter):
        return ord(letter) - ord('a')

    def getStrHash(self, text, size):
        if size <= 0:
            return

        hashValue = 0
        for idx, char in enumerate(text):
            if idx == size:
                return hashValue
            hashValue = (hashValue * self.PRIME +
                         self.getCharHash(char)) % self.mod

        return hashValue
