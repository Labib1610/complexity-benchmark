import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    primary = list(map(int, sys.stdin.readline().split()))
    
    # Convert to 0-indexed
    primary = [x - 1 for x in primary]
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u-1, v-1))
    
    if t <= 1:
        print(0)
        return
    
    # Sort edges by weight
    edges.sort()
    
    # Union-Find data structure
    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    # Kruskal's algorithm variant
    total_cost = 0
    components = t
    
    for cost, u, v in edges:
        if find(u) != find(v):
            if union(u, v):
                # Check if any two primary registers are now connected
                connected = set()
                for p in primary:
                    connected.add(find(p))
                
                if len(connected) < components:
                    components = len(connected)
                    total_cost += cost
                    
                if components == 1:
                    break
    
    print(total_cost)

threading.Thread(target=main).start()