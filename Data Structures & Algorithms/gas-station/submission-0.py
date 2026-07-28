import heapq

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1

        for s in range(n):
            if self.dijkstra_check(s, gas, cost):
                return s
        return -1

    def dijkstra_check(self, k, gas, cost):
        n = len(gas)

        dist = {i: float('inf') for i in range(n)}
        dist[k] = 0
        heap = [(0, k)]
        visited = set()

        while heap:
            d, u = heapq.heappop(heap)

            if u in visited:
                continue
            visited.add(u)

            if d > dist[u]:
                continue

            if d > 0:
                return False

            if len(visited) >= n:
                break

            v = (u + 1) % n
            w = cost[u] - gas[u]
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

        return True