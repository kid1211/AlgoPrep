class Solution:
    """
    @param graph: a list of Undirected graph node
    @param A: nodeA
    @param B: nodeB
    @return:  the length of the shortest path
    """

    def shortestPath(self, graph, A, B):
        # Write your code here
        if A == B:
            return 0

        queue = collections.deque([A])
        visited = set()
        steps = 0

        while queue:
            steps += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in node.neighbors:

                    if neighbor in visited:
                        continue

                    if neighbor == B:
                        return steps

                    visited.add(neighbor)
                    queue.append(neighbor)

        return -1


# {1,2,3,4#2,1,3#3,1#4,1,5#5,4}
# 1
# 5

# {1,2,4#2,1,4#3,5#4,1,2#5,3}
# 3
# 5
