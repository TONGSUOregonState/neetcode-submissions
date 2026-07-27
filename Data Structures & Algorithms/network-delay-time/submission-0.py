import heapq
from collections import defaultdict
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 缺这部分1：建图
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 缺这部分2：初始化dist和heap
        dist = {i: float('inf') for i in range(1, n+1)}
        dist[k] = 0
        heap = [(0, k)]
        
        # 你已经写好的部分，接在这里
        while heap :
            d,u = heapq.heappop(heap)
            
            if d > dist[u]:
                continue
            
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap,(dist[v],v))
        
        max_dist = max(dist.values())
        return max_dist if max_dist < float('inf') else -1