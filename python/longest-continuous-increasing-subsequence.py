class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """

    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        if not A:
            return 0

        longest = 0
        inc = dec = 0

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                inc += 1
                dec = 0
            else:
                inc = 0
                dec += 1
            longest = max(inc, dec, longest)
        return longest + 1
