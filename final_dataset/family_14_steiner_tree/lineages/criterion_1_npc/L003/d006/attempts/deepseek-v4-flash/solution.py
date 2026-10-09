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
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))

    targets = [int(next(it)) - 1 for _ in range(t)]

    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((w, u, v))

    edges.sort()

    dsu = DSU(n)
    target_set = set(targets)
    # Count how many target components we have initially
    target_roots = set(dsu.find(x) for x in targets)
    components_needed = len(target_roots)

    total_cost = 0
    for w, u, v in edges:
        if components_needed == 1:
            break
        ru, rv = dsu.find(u), dsu.find(v)
        if ru != rv:
            # Check if this union merges two different target components
            before = set()
            for x in targets:
                before.add(dsu.find(x))
            dsu.union(u, v)
            after = set()
            for x in targets:
                after.add(dsu.find(x))
            if len(after) < len(before):
                total_cost += w
                components_needed = len(after)

    print(total_cost)

if __name__ == "__main__":
    main()