class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def dropEggs(self, n):
        # write your code here
        # 1 more than before
        res, count = 1, 1

        while res < n:
            count += 1
            res += count

        return count
