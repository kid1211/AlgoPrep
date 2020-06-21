class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        # write your code here
        left, right = 0, x

        while left + 1 < right:
            mid = (left + right) // 2
            midSquare = mid * mid

            if midSquare == x:
                return mid
            elif midSquare > x:
                right = mid
            else:
                left = mid

        if right * right <= x:
            return right

        if left * left <= x:
            return left
