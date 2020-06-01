class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """

    def minWindow(self, source, target):
        n = len(source)
        tarLength = len(target)
        minimum = source + "1"
        j = 0

        targetSet = {}
        for tar in target:
            if tar not in targetSet:
                targetSet[tar] = (0, 1)
                continue
            _, required = targetSet[tar]
            targetSet[tar] = (0, required + 1)

        for i in range(n):
            while j < n and not self.didFindAllTaget(targetSet, tarLength):
                if source[j] in targetSet:
                    current, required = targetSet[source[j]]
                    targetSet[source[j]] = (current + 1, required)
                j += 1
            if self.didFindAllTaget(targetSet, tarLength):
                text = source[i:j]
                if len(text) < len(minimum):
                    minimum = text

            takeOut = source[i]
            if takeOut in targetSet:
                current, required = targetSet[takeOut]
                targetSet[takeOut] = (current - 1, required)

        return "" if len(minimum) > n else minimum

    def didFindAllTaget(self, targetSet, tarLength):
        length = 0
        for key in targetSet:
            current, required = targetSet[key]
            if current > required:
                length += required
            else:
                length += current

        return length >= tarLength


# "abcdecf"
# "acc"
# "absdfaabab"
# "adb"
