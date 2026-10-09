import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.has_reserve = [False] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.rank[xr] < self.rank[yr]:
            xr, yr = yr, xr
        self.parent[yr] = xr
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1
        self.has_reserve[xr] = self.has_reserve[xr] or self.has_reserve[yr]
        return True

def main():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    reserves = list(map(int, input().split()))
    reserve_set = set(reserves)

    dsu = DSU(n)
    for r in reserves:
        dsu.has_reserve[r - 1] = True

    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u - 1, v - 1))

    edges.sort()

    total_cost = 0
    connected_reserves = 0
    # Count initial reserve components
    seen = set()
    for r in reserves:
        root = dsu.find(r - 1)
        if root not in seen:
            seen.add(root)
            connected_reserves += 1

    for w, u, v in edges:
        if connected_reserves == 1:
            break
        ru, rv = dsu.find(u), dsu.find(v)
        if ru == rv:
            continue
        # Only connect if at least one component has a reserve
        if dsu.has_reserve[ru] and dsu.has_reserve[rv]:
            dsu.union(ru, rv)
            total_cost += w
            connected_reserves -= 1
        elif dsu.has_reserve[ru] or dsu.has_reserve[rv]:
            dsu.union(ru, rv)
            total_cost += w
            # If one side had reserve, the merged component still has reserve
            # connected_reserves count stays same if only one had reserve
        # If neither has reserve, skip (no need to connect)

    print(total_cost)

if __name__ == "__main__":
    main()