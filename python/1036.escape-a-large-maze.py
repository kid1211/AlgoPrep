#
# @lc app=leetcode id=1036 lang=python3
#
# [1036] Escape a Large Maze
#

# @lc code=start
from heapq import heappush, heappop

# 20000
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if len(blocked) == 0:
            return True
        DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        target = tuple(target)
        source = tuple(source)

        visited = set()
        for block in blocked:
            visited.add(tuple(block))

        queue = [(self.getDistance(source, target), source)]

        while queue:
            _, current = heappop(queue)
            # print(current, target)
            if current == target:
                return True

            visited.add(current)
            for dir in DIRECTION:
                nextStep = (current[0] + dir[0], current[1] + dir[1])

                if nextStep in visited or not self.isValid(nextStep):
                    continue
                visited.add(nextStep)
                distant = self.getDistance(nextStep, target)
                heappush(queue, (distant, nextStep))
                if len(queue) >= 20000:
                    return True
            # if len(queue) >= 10000:
            #     return True
        # print('wtf?')
        return False

    def getDistance(self, nextStep, target):
        nextX, nextY = nextStep
        tarX, tarY = target
        x = (nextX - tarX)
        y = (nextY - tarY)
        return sqrt(x*x + y*y)

    def isValid(self, nextStep):
        x, y = nextStep
        return x >= 0 and x < 1000000 and y >= 0 and y < 1000000


# @lc code=end
[[691938, 300406], [710196, 624190], [858790, 609485], [268029, 225806], [200010, 188664], [132599, 612099], [329444, 633495], [196657, 757958], [628509, 883388]]\n[655988, 180910]\n[267728, 840949]
