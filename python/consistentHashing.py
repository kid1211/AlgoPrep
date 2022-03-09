class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """

    def consistentHashing(self, n):
        # write your code here

        res = [
            [0, 359, 1]
        ]
        for idx in range(2, n + 1):
            self.addDB(res, idx)
        return res

    def addDB(self, res, idx):
        # fin the lagest first
        maxDiff, largest = 0, None

        for i in range(len(res)):
            diff = res[i][1] - res[i][0]
            if diff > maxDiff:
                maxDiff, largest = diff, i
        print(largest)

        # cut the size in half
        takingApart = res[largest]
        newEnd = takingApart[0] + maxDiff // 2
        res.append([newEnd + 1, takingApart[1], idx])
        res[largest] = [takingApart[0], newEnd, takingApart[2]]
        return res
