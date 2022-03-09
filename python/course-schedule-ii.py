class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree, maps = self.getIndegreeAndRelationship(
            numCourses, prerequisites)

        # construct graph
        res = []
        queue = collections.deque([n for n in indegree if indegree[n] == 0])

        while queue:
            course = queue.popleft()
            res.append(course)

            for node in maps[course]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)

        return res if len(res) == numCourses else []

    def getIndegreeAndRelationship(self, numCourses, prerequisites):
        indegree = {n: 0 for n in range(numCourses)}
        maps = collections.defaultdict(list)

        for (course, preReq) in prerequisites:
            maps[preReq].append(course)  # once preReq is finish you can enable
            indegree[course] += 1

        return indegree, maps
