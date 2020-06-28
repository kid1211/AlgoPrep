class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        if not height:
            return 0

        n = len(height)
        stack = []

        def insert(idx, maxRec):
            val = height[idx] if idx != n else -sys.maxsize + 1

            while stack and val < height[stack[-1]]:
                pop = stack.pop()
                lower = stack[-1] + 1 if stack else 0
                area = height[pop] * (idx - lower)  # maybe?
                # print(maxRec, stack, idx, pop, lower, height[pop] * (idx - lower) )
                maxRec = max(maxRec, area)

            if idx != n:
                stack.append(idx)
            return maxRec

        maxRec = 0
        for idx in range(len(height)):
            maxRec = insert(idx, maxRec)

        while stack:
            maxRec = insert(n, maxRec)

        return maxRec


# [2,1,5,6,2,3]
# [5,4,1,2]

#
