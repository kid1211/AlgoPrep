class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        # write your code here
        sortingWithDict = {}

        for item in colors:
            if not item in sortingWithDict:
                sortingWithDict[item] = 1
            else:
                sortingWithDict[item] += 1

        for i in range(1, k + 1):
            if not i in sortingWithDict:
                continue
            rtn += ([i] * sortingWithDict[i])

        for i in range(len(colors)):
            colors[i] = rtn[i]
