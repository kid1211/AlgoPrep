class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """

    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        if not A:
            return 0

        longest, inc, dec = 1, 1, 1
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                inc += 1
                dec = 1
            elif A[i] < A[i - 1]:
                dec += 1
                inc = 1
            else:
                inc, dec = 1, 1
            longest = max(longest, inc, dec)
        return longest
