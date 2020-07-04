class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """

    def trapRainWater(self, heights):
        # write your code here
        left, right = 0, len(heights) - 1

        if right < 0:
            return 0

        leftMax, rightMax = heights[left], heights[right]

        def getSums(idx, maxVal, sums):
            maxVal = max(maxVal, heights[idx])
            sums += maxVal - heights[idx]
            return maxVal, sums

        sums = 0
        while left <= right:
            if leftMax < rightMax:
                leftMax = max(leftMax, heights[left])
                sums += leftMax - heights[left]
                left += 1
            else:
                rightMax = max(rightMax, heights[right])
                sums += rightMax - heights[right]
                right -= 1

        return sums
