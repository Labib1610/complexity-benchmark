import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    try:
        n = int(next(it))
        m = int(next(it))
        k = int(next(it))
        B = int(next(it))
    except StopIteration:
        return

    anomalies = set()
    for _ in range(k):
        try:
            anomalies.add(int(next(it)))
        except StopIteration:
            return

    edges = []
    for _ in range(m):
        try:
            u = int(next(it))
            v = int(next(it))
            w = int(next(it))
            edges.append((u, v, w))
        except StopIteration:
            return

    # DSU for Kruskal's algorithm
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    total_cost = 0
    result_edges = []

    for u, v, w in edges:
        if find(u) != find(v):
            # Check if merging would connect two anomalies
            # We need to check if the component of u contains an anomaly
            # and the component of v contains an anomaly
            # Since we track roots, we need to check if both roots are in anomaly_roots
            # But we don't track anomaly_roots, so we check differently
            
            # Actually, let's track which components have anomalies
            # We can use a separate set or array
            pass

    # Let's restart with proper tracking of anomaly components
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    has_anomaly = [False] * (n + 1)
    for a in anomalies:
        has_anomaly[a] = True

    def find_with_anomaly(x):
        # Regular find, but we need to track anomaly status
        # Actually, we track anomaly status separately
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    total_cost = 0
    result_edges = []

    for u, v, w in edges:
        ru, rv = find_with_anomaly(u), find_with_anomaly(v)
        if ru != rv:
            # Check if both components have anomalies
            if has_anomaly[ru] and has_anomaly[rv]:
                # This edge must be collapsed
                total_cost += w
                result_edges.append((u, v))
                if total_cost > B:
                    print("NO")
                    return
            else:
                # Safe to merge
                # Union by rank
                if rank[ru] < rank[rv]:
                    parent[ru] = rv
                    has_anomaly[rv] = has_anomaly[rv] or has_anomaly[ru]
                elif rank[ru] > rank[rv]:
                    parent[rv] = ru
                    has_anomaly[ru] = has_anomaly[ru] or has_anomaly[rv]
                else:
                    parent[rv] = ru
                    has_anomaly[ru] = has_anomaly[ru] or has_anomaly[rv]
                    rank[ru] += 1

    print("YES")
    print(len(result_edges))
    for u, v in result_edges:
        print(u, v)

if __name__ == "__main__":
    solve()