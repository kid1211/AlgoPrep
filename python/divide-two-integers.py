class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX
        neg = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
        a, b = abs(dividend), abs(divisor)
        ans = 0
        for i in range(31, -1, -1):
            if a == 0:
                break
            if a >= b << i:
                a -= b << i  # b << i = b * 2** i, every time << 1, it means times 2
                ans += 1 << i  # 1 << i = 2**i

        if neg:
            ans = - ans
        if ans > INT_MAX:
            return INT_MAX
        return ans
