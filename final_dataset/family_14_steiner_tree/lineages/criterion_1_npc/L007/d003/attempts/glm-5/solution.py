import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    priority = set()
    for _ in range(t):
        priority.add(int(next(it)))
    
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
    edges.sort()
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
    
    total_cost = 0
    components = n
    
    for w, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            total_cost += w
            components -= 1
            
            # Check if all priority nodes are connected
            it_priority = iter(priority)
            first_p = next(it_priority)
            root = find(first_p)
            all_connected = True
            for p in it_priority:
                if find(p) != root:
                    all_connected = False
                    break
            if all_connected:
                print(total_cost)
                return
    
    print(total_cost)

if __name__ == "__main__":
    solve()