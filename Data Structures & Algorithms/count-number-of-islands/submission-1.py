class unionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    def find(self,x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    def union(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        if self.rank[rx]< self.rank[ry]:
            rx,ry = ry,rx
        self.parent[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        
        uf = unionFind()
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == '1':
                    if column + 1 < columns and grid[row][column+1]=='1':
                        uf.union((row, column), (row, column + 1))
                    if row+1 < rows and grid[row+1][column] == '1':
                        uf.union((row, column), (row+1, column))
        root = set()
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == '1':
                    root.add(uf.find((row, column)))
        return len(root)




