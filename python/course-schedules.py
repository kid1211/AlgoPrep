class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        (indegrees, enablingCourse) = self.getIndegreesMap(numCourses, prerequisites) # good

        
        # even there is duplicate, if you decided to remove it , 
        # you can remove both at two times same thing
        zeroDependency = [course for course in indegrees if indegrees[course] == 0]
        queue = collections.deque(zeroDependency)
        
        results = []
        while queue:
            course = queue.popleft()
            results.append(course)
            
            for openedCourse in enablingCourse[course]:
                indegrees[openedCourse] -= 1
                if indegrees[openedCourse] == 0:
                    queue.append(openedCourse)
            
            # what courses can be done now
        return len(results) == numCourses
        
    def getIndegreesMap(self, numCourses, prerequisites):
        indegrees = { n: 0 for n in range(numCourses) }
        enablingCourse = { n: [] for n in range(numCourses) }
        
        for (course, prereq) in prerequisites:
            indegrees[course] += 1
            enablingCourse[prereq].append(course)
            
        return (indegrees, enablingCourse)
# 10
# [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]