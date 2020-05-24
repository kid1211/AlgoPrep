from heapq import heappush, heappop, heapify


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        # Write your code here
        # so we will need to know the list of all the characters
        # graph

        graph = self.buildGraph(words)
        # print(graph)
        return self.topo_sort(graph)

        # word in words construct a graph
    def buildGraph(self, words):
        graph = {}

        # init graph
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = set()

        # add edges, while look could have work too
        for i in range(len(words) - 1):
            start = min(len(words[i]), len(words[i + 1]))
            for j in range(start):
                if words[i][j] != words[i + 1][j]:
                    # so that the next one come after
                    graph[words[i][j]].add(words[i + 1][j])
                    break
        return graph

    def topo_sort(self, graph):
        indegrees = self.getIndegrees(graph)
        # print(indegrees)

        # use heap instead of quueue to met that results
        queue = [n for n in indegrees if indegrees[n] == 0]
        heapify(queue)

        results = []
        while queue:
            node = heappop(queue)
            results.append(node)

            for edge in graph[node]:
                indegrees[edge] -= 1
                if indegrees[edge] == 0:
                    heappush(queue, edge)

        if len(results) != len(indegrees):
            return ""
        return "".join(results)

    def getIndegrees(self, graph):
        indegrees = {n: 0 for n in graph}

        for node in graph:
            for edge in graph[node]:
                indegrees[edge] += 1
        return indegrees


# BELOW is not working but it can be used to compare queue vs heap
# class Solution:
#     """
#     @param words: a list of words
#     @return: a string which is correct order
#     """

#     def alienOrder(self, words):
#         # Write your code here
#         # so we will need to know the list of all the characters
#         # graph

#         graph = self.buildGraph(words)
#         # print(graph)
#         return self.topo_sort(graph)

#         # word in words construct a graph
#     def buildGraph(self, words):
#         graph = {}

#         # init graph
#         for word in words:
#             for char in word:
#                 if char not in graph:
#                     graph[char] = set()

#         # add edges
#         for i in range(len(words) - 1):
#             start = min(len(words[i]), len(words[i + 1]))
#             for j in range(start):
#                 if words[i][j] != words[i + 1][j]:
#                     # so that the next one come after
#                     graph[words[i][j]].add(words[i + 1][j])
#                     break
#         return graph

#     def topo_sort(self, graph):
#         indegrees = self.getIndegrees(graph)
#         print(indegrees)
#         start = [n for n in indegrees if indegrees[n] == 0]
#         queue = collections.deque(start)

#         results = []
#         while queue:
#             node = queue.popleft()
#             results.append(node)

#             for edge in graph[node]:
#                 indegrees[edge] -= 1
#                 if indegrees[edge] == 0:
#                     queue.append(edge)

#         if len(results) != len(indegrees):
#             return ""
#         return "".join(results)

#     def getIndegrees(self, graph):
#         indegrees = {n: 0 for n in graph}

#         for node in graph:
#             for edge in graph[node]:
#                 indegrees[edge] += 1
#         return indegrees

# # compare
# # ["wrt","wrf","er","ett","rftt"]
# # ["zy","zx"]
