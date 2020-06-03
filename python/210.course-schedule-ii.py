#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree, enablers = self.getIndegree(numCourses, prerequisites)

        queue = collections.deque([c for c in inDegree if inDegree[c] == 0])
        rtn = []
        while queue:
            course = queue.popleft()
            rtn.append(course)
            for co in enablers[course]:
                inDegree[co] -= 1
                if inDegree[co] == 0:
                    queue.append(co)

        return [] if len(rtn) != numCourses else rtn

    def getIndegree(self, n, prerequisites):

        inDegree, enablers = {}, {}
        for i in range(n):
            inDegree[i] = 0
            enablers[i] = []

        for (course, prereq) in prerequisites:
            inDegree[course] += 1
            enablers[prereq].append(course)
        return inDegree, enablers
# @lc code=end
