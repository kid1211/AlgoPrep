class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # This is genius act
        # imagine a tree, also this catch an issue
        # when there is two part of a graph
        if len(edges) != n - 1:
            return False

        neighbors = collections.defaultdict(list)
        for left, right in edges:
            neighbors[left].append(right)
            neighbors[right].append(left)

        # because there is no direction, so no idegree
        # visited get out of cyclone, and catch graph node not being visited
        visited = set()
        queue = collections.deque([0])

        while queue:
            node = queue.popleft()
            visited.add(node)
            for edge in neighbors[node]:
                if edge in visited:
                    continue
                visited.add(edge)
                queue.append(edge)

        return len(visited) == n

# 10
# [[0,1],[5,6],[6,7],[9,0],[3,7],[4,8],[1,8],[5,2],[5,3]]
