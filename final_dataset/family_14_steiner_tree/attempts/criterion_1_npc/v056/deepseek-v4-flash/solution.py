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
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True

def main():
    import sys
    input = sys.stdin.readline

    n, m, t = map(int, input().split())
    core = list(map(int, input().split()))
    core_set = set(core)

    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u - 1, v - 1))

    edges.sort()

    dsu = DSU(n)
    total_cost = 0
    connected = 0

    # We need to connect all core nodes together
    target = t - 1  # number of unions needed to connect t nodes

    for w, u, v in edges:
        if dsu.union(u, v):
            # Check if this union helped connect core nodes
            # We can just count unions among core nodes' components
            total_cost += w
            connected += 1
            if connected >= target:
                # But we must ensure all core nodes are in the same component
                # Check if all core nodes have same root
                root = dsu.find(core[0] - 1)
                if all(dsu.find(c - 1) == root for c in core):
                    print(total_cost)
                    return

    # If not returned yet, print the accumulated cost (shouldn't happen per problem statement)
    print(total_cost)

if __name__ == "__main__":
    main()