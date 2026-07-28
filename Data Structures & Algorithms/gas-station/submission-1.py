class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1

        for s in range(n):
            if self.check(s, gas, cost):
                return s
        return -1

    def check(self, k, gas, cost):
        n = len(gas)

        dist = {i: float('inf') for i in range(n)}
        dist[k] = 0

        u = k
        for _ in range(n):   # 路径唯一确定,直接走n步,不用heap
            if dist[u] > 0:   # 累计代价一旦变正,说明中途亏空
                return False

            v = (u + 1) % n
            w = cost[u] - gas[u]
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

            u = v   # 直接顺着走到下一个节点,不需要从堆里挑

        return True