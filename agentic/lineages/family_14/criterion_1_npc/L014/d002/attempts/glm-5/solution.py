import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    critical = set()
    for _ in range(t):
        critical.add(int(next(it)))
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    # Kruskal's algorithm
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
    
    edges.sort()
    total_cost = 0
    components = t
    
    for w, u, v in edges:
        if union(u, v):
            total_cost += w
            # Check if all critical nodes are connected
            # Get the root of the first critical node
            root = find(next(iter(critical)))
            all_connected = True
            for node in critical:
                if find(node) != root:
                    all_connected = False
                    break
            if all_connected:
                print(total_cost)
                return
    
    print(total_cost)

if __name__ == "__main__":
    solve()