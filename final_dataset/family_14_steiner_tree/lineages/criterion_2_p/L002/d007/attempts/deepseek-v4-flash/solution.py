import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

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
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1
        return True

def main():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = set(map(int, input().split()))
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u-1, v-1))
    edges.sort()

    dsu = DSU(n)
    target_count = len(targets)
    # We'll track how many target nodes are in each component
    comp_target_count = [0] * n
    for idx in targets:
        comp_target_count[idx-1] = 1

    total_cost = 0
    connected_targets = 0
    for w, u, v in edges:
        ru, rv = dsu.find(u), dsu.find(v)
        if ru != rv:
            # union
            if dsu.rank[ru] < dsu.rank[rv]:
                ru, rv = rv, ru
            dsu.parent[rv] = ru
            if dsu.rank[ru] == dsu.rank[rv]:
                dsu.rank[ru] += 1
            comp_target_count[ru] += comp_target_count[rv]
            total_cost += w
            if comp_target_count[ru] == target_count:
                print(total_cost)
                return

if __name__ == "__main__":
    main()