import sys
import heapq
from collections import defaultdict

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

def main():
    n, m, t = map(int, sys.stdin.readline().split())
    hubs = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    # Sort edges by weight
    edges.sort()
    
    # We need to find the minimum spanning tree that connects all hubs
    # We'll use a modified Kruskal's algorithm
    
    # Initially, each node is its own component
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    total_cost = 0
    connected_hubs = {hub: hub for hub in hubs}
    
    for w, u, v in edges:
        if union(parent, rank, u, v):
            total_cost += w
            # Check if all hubs are now connected
            root = find(parent, hubs[0])
            if all(find(parent, hub) == root for hub in hubs):
                break
    
    print(total_cost)

if __name__ == "__main__":
    main()