class UnionFind:
    def __init__(self):
        self.parent: dict[str, str] = {}
        self.weight: dict[str, float] = {}

    def find(self, x: str) -> str:
        if x not in self.parent:
            self.parent[x] = x
            self.weight[x] = 1.0
        if self.parent[x] != x:
            root = self.find(self.parent[x])
            self.weight[x] *= self.weight[self.parent[x]]
            self.parent[x] = root
        return self.parent[x]

    def union(self, a: str, b: str, val: float) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        self.parent[ra] = rb
        self.weight[ra] = val * self.weight[b] / self.weight[a]


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                      queries: List[List[str]]) -> List[float]:
        uf = UnionFind()
        for (a, b), val in zip(equations, values):
            uf.union(a, b, val)

        res = []
        for c, d in queries:
            if c not in uf.parent or d not in uf.parent:
                res.append(-1.0)
                continue
            rc, rd = uf.find(c), uf.find(d)
            res.append(uf.weight[c] / uf.weight[d] if rc == rd else -1.0)
        return res