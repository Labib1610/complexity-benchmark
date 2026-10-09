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

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return True

def main():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = list(map(int, input().split()))
    critical_set = set(critical)

    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u - 1, v - 1))

    if t <= 1:
        print(0)
        return

    edges.sort()
    dsu = DSU(n)
    total_cost = 0
    critical_connected = {x: False for x in critical_set}
    # We need to connect all critical nodes into one component
    # Use Kruskal but only care about connecting critical nodes
    # We can stop when all critical nodes are in the same component
    critical_list = critical
    target = critical_list[0]
    for w, u, v in edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            total_cost += w
            # check if all critical nodes are connected
            root = dsu.find(target)
            all_connected = True
            for c in critical_list:
                if dsu.find(c) != root:
                    all_connected = False
                    break
            if all_connected:
                print(total_cost)
                return

    # If not all connected (shouldn't happen because graph is connected)
    print(total_cost)

if __name__ == "__main__":
    main()