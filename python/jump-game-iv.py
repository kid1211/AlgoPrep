class Solution:
    def minJumps(self, arr: List[int]) -> int:
        jumps = collections.defaultdict(list)
        n = len(arr)
        for i in range(n):
            jumps[arr[i]].append(i)

        curs = collections.deque([0])  # start
        visited = set([0])
        steps = -1

        while curs:
            steps += 1
            for _ in range(len(curs)):
                node = curs.popleft()

                if node == n - 1:
                    return steps

                for child in jumps[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        curs.append(child)
                del jumps[arr[node]]

                for child in [node - 1, node + 1]:
                    if 0 <= child < n and child not in visited:
                        visited.add(child)
                        curs.append(child)

        return -1