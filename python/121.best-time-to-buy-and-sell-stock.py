#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, lowest = 0, sys.maxsize

        for num in prices:
            maxProfit = max(num - lowest, maxProfit)
            lowest = min(num, lowest)

        return maxProfit

# @lc code=end
