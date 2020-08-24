class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        if not times:
            return 0

        graph = collections.defaultdict(list)
        for s, d, cost in times:
            graph[s].append((d, cost))
        heap, closest, dist = [(0, K)], set(), {}

        while heap:
            cost, target = heapq.heappop(heap)

            if target in closest:
                continue
            closest.add(target)
            dist[target] = cost

            for nextP, nextCost in graph[target]:
                print(nextP, nextCost)
                if nextP in closest:
                    continue

                if nextP in dist and dist[nextP] < cost + nextCost:
                    continue

                dist[nextP] = cost + nextCost
                heapq.heappush(heap, (cost + nextCost, nextP))
        return max(dist.values()) if len(dist) == N else -1
