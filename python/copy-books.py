class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0
        left, right = max(pages), sum(pages)

        while left <= right:
            mid = (left + right) // 2

            if self.calculateK(pages, mid) > k:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def calculateK(self, pages, time):
        count = currentSum = 0

        for page in pages:
            if page + currentSum > time:
                currentSum = 0
                count += 1
            currentSum += page
        return count + 1
