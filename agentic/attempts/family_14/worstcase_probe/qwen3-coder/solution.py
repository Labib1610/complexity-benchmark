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

def kruskal(n, edges, required):
    parent = list(range(n))
    rank = [0] * n
    result = []
    cost = 0
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    for u, v, w in edges:
        if union(parent, rank, u, v):
            result.append((u, v))
            cost += w
            if len(result) == n - 1:
                break
    
    # Check if all required nodes are connected
    if not required:
        return True, [], 0
    
    req_parent = find(parent, required[0])
    for node in required:
        if find(parent, node) != req_parent:
            return False, [], 0
            
    return True, result, cost

def solve():
    line = input().split()
    n, m, t, B = int(line[0]), int(line[1]), int(line[2]), int(line[3])
    
    if t == 0:
        print("YES")
        return
        
    required = list(map(int, input().split()))
    required = [r - 1 for r in required]  # Convert to 0-indexed
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u-1, v-1, w))  # Convert to 0-indexed
    
    # Try to find minimum spanning tree
    connected, mst_edges, total_cost = kruskal(n, edges, required)
    
    if not connected or total_cost > B:
        print("NO")
        return
    
    # Now we need to find a subtree that connects all required nodes with cost <= B
    # We'll use a different approach: build a Steiner tree approximation
    
    # For simplicity, let's try pruning the MST to get a subtree connecting required nodes
    # But first check if the full MST is within budget
    if total_cost <= B:
        print("YES")
        for u, v in mst_edges:
            print(u + 1, v + 1)  # Convert back to 1-indexed
        return
    
    # If MST exceeds budget, it's impossible since MST is minimum
    print("NO")

# Run the solution
solve()