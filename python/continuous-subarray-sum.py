class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def continuousSubarraySum(self, A):
        # write your code here
        maxi = -sys.maxsize + 1
        mini, miniIdx = 0, -1
        rollingSum = 0

        for i in range(len(A)):
            rollingSum += A[i]
            if rollingSum - mini > maxi:
                maxi = rollingSum - mini
                res = [miniIdx + 1, i]
            if mini > rollingSum:
                mini = rollingSum
                miniIdx = i
        return res
