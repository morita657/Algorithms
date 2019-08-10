from collections import defaultdict

# Dijkstra's


class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = defaultdict(list)
        # print graph
        # make graph  = [(destination, weight) ], index is start point
        for u, v, w in times:
            graph[u].append((v, w))
        # intialization
        dist = {node: float('inf') for node in xrange(1, N + 1)}
        seen = [False] * (N + 1)
        # start point is K
        dist[K] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')
            # cand_dist and cand_node specification
            for i in xrange(1, N + 1):
                # if the current location cost is bigger than the adjacent location,
                # move it the next cheapest location
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i
            # there is the edge case, leave the loop
            if cand_node < 0:
                break
            # mark the location as visited
            seen[cand_node] = True
            # explore the neighborhood and find the cheapest location
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1


s = Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
print(s)


# Bellman-Ford

class Solution(object):
    def networkDelayTime(self, times, N, K):
        dist = {node: float('inf') for node in xrange(1, N + 1)}
        dist[K] = 0
        for u, v, w in times:
            dist[v] = min(dist[v], dist[u] + w)
        res = -1
        for key in dist:
            res = max(dist[key], res)
        return res if res < float('inf') else -1


s = Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
print(s)

import heapq


class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d + d2, nei))

        return max(dist.values()) if len(dist) == N else -1


s = Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
print(s)
