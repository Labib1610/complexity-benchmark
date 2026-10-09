import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    n, m, t = map(int, sys.stdin.readline().split())
    flagged = set(map(int, sys.stdin.readline().split()))
    
    # If there's only one flagged module, no relays needed
    if t <= 1:
        print(0)
        return
    
    # Build the tree
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((w, u, v))
    
    # Sort edges by weight for Kruskal's algorithm
    edges.sort()
    
    # Union-Find data structure
    parent = list(range(n + 1))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    # Kruskal's algorithm to find the minimum spanning tree that connects all flagged modules
    total_energy = 0
    flagged_count = 0
    
    for w, u, v in edges:
        if union(u, v):
            total_energy += w
            # Check if all flagged modules are now connected
            roots = set(find(x) for x in flagged)
            if len(roots) == 1:
                break
    
    print(total_energy)

if __name__ == "__main__":
    main()