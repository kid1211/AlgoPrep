#
# @lc app=leetcode id=686 lang=python3
#
# [686] Repeated String Match
#

# @lc code=start
PRIME = 41
MOD = sys.maxsize // PRIME


class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        # A x something
        init = len(B) // len(A)
        C = "".join([A * init])
        print(self.isMatch("aac", "aaac"))
        # "cabca"
        # "abc"
        for count in range(init, init + 3):
            # print(B, C)
            if B in C:
                return count
            # print(B, C)
            # if self.isMatch(B, C):
            #     return count
            C += A
        return -1

    def isMatch(self, tar, src):
        if len(src) < len(tar):
            return False

        def letterVal(l):
            return ord(l) - ord('a')

        tgtHash = 0
        srcHash = 0
        highCoefficient = PRIME ** (len(tar) - 1)  # stuck here
        tarLength = len(tar)

        for i in range(len(tar)):
            tgtHash = tgtHash * PRIME + letterVal(tar[i])
            srcHash = srcHash * PRIME + letterVal(src[i])
            tgtHash %= MOD
            srcHash %= MOD

        if tgtHash == srcHash and src[0: tarLength] == tar:
            return True

        for idx in range(len(tar), len(src)):
            if tgtHash == srcHash and src[idx - tarLength: idx] == tar:
                return True

            srcHash -= highCoefficient * letterVal(src[idx - tarLength])
            srcHash *= PRIME
            srcHash += letterVal(src[idx])
            srcHash %= MOD
        return False
# @lc code=end


"abcd"
"cdabcdab"
