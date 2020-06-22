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
        start, end = max(pages), sum(pages)

        while start + 1 < end:
            mid = (start + end) // 2

            if self.requiredPeople(pages, mid) <= k:
                end = mid
            else:
                start = mid

        if self.requiredPeople(pages, start) <= k:
            return start
        return end

    def requiredPeople(self, pages, timeLimit):
        count = 0

        timeSpent = 0
        for page in pages:
            if timeSpent + page > timeLimit:
                count += 1
                timeSpent = 0
            timeSpent += page

        return count + 1
