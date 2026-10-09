n, m = map(int, input().split())

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
        return True

total = 0
dsu = DSU(n)
for w, u, v in edges:
    if dsu.find(u) != dsu.find(v):
        total += w
        dsu.union(u, v)

print(total)